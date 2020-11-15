#!/bin/bash

pip install --upgrade pip
pip install --upgrade PyNaCl
pip install --upgrade discord.py
pip install --upgrade youtube-dl
apt-get update && apt-get install -y ffmpeg

trap 'trap " " SIGTERM; echo "SIGTERM received by shell"; kill 0; wait' SIGTERM

python /houseband/bot_main.py &

wait