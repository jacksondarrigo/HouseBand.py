import discord
from discord.ext import commands
import signal
import asyncio
import time
import sys
import os

TOKEN = os.environ.get('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!!!', case_insensitive=True, description="HouseBand Music Bot")

cogs = ['music']

#
# EVENTS
#

@bot.event
async def on_ready():
    print("\nHouseBand Online\n")
    guilds = bot.guilds
    names = '\n'.join([guild.name for guild in guilds])
    print("Serving the following guilds: \n" + names + "\n")

@bot.event
async def on_command(context):
    now = time.strftime("%x %X")
    guild = context.guild
    author = context.message.author
    content = context.message.content
    print('[{}]({}) {}: {}\n'.format(now, guild, author, content))

@bot.event
async def on_command_error(context, exception):
    await context.send('Command failed. ({})'.format(exception))

if __name__ == '__main__':
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print('{} successfully loaded.'.format(cog))
        except Exception as error:
            print('{} cannot be loaded. ({})'.format(cog, error))

    async def close(bot):
        """|coro|
        Closes the connection to Discord.
        """
        if bot._closed:
            return
        
        await bot.http.close()

        if bot.ws is not None and bot.ws.open:
            await bot.ws.close(code=1000)

        bot._closed = True
    
        for voice in bot.voice_clients:
            try:
                await voice.disconnect()
            except Exception:
                # if an error happens during disconnects, disregard it.
                pass
    
        bot._ready.clear()

    #async def sigterm_handler():
    #    await bot.change_presence(status=discord.Status.offline)
    #    await bot.close()

    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGTERM, lambda: asyncio.create_task(close(bot)))
    loop.run_until_complete(bot.start(TOKEN))