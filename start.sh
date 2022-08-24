#!/bin/env bash
cd $(dirname $0)
export DISPLAY=:0.0
rm /home/tsic/package/downloads/*
nohup ./venv/bin/python3 ./main.py >> /tmp/auto_log&
