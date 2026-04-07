#!/bin/bash

cd ~/devops-health-dashboard

# Pull latest code
git pull

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Stop existing Flask app
pkill -f app.py || true

# Start app in background
nohup python app/app.py > output.log 2>&1 &