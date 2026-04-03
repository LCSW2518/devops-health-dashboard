#!/bin/bash
cd ~/devops-health-dashboard
git pull
pip3 install -r requirements.txt
pkill -f app.py || true
nohup python3 app/app.py > output.log 2>&1 &