#!/usr/bin/env bash

pip install --upgrade pip
pip install --upgrade PyNaCl
pip install --upgrade discord.py
pip install --upgrade youtube-dl
dnf install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
dnf install --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm
dnf install --nogpgcheck https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm
dnf config-manager --enable PowerTools
dnf install ffmpeg

trap 'trap " " SIGTERM; kill 0; wait' SIGTERM

python /houseband/bot_main.py &

wait
