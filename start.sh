#!/usr/bin/env bash

pip install --upgrade pip
pip install --upgrade PyNaCl
pip install --upgrade discord.py
pip install --upgrade youtube-dl
yum install epel-release
yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
yum install ffmpeg

trap 'trap " " SIGTERM; kill 0; wait' SIGTERM

python /houseband/bot_main.py &

wait
