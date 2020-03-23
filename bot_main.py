from discord.ext import commands
import time

tokenFile = open("./credentials.txt")
TOKEN = tokenFile.read()
TOKEN = TOKEN.strip()
tokenFile.close()

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

    bot.run(TOKEN)