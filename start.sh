#!/bin/bash

echo $1

pip install --upgrade pip
pip install --upgrade PyNaCl
pip install --upgrade discord.py
pip install --upgrade youtube-dl
apt-get update && apt-get install -y ffmpeg

python /houseband/bot_main.py $1