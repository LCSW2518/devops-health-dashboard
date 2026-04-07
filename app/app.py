from flask import Flask, render_template
import datetime
import socket
import subprocess
import psutil
import platform

app = Flask(__name__)

start_time = datetime.datetime.now()

def get_git_version():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"]
        ).decode().strip()
    except:
        return "N/A"

@app.route('/')
def home():
    uptime = datetime.datetime.now() - start_time
    hostname = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    version = get_git_version()

    # System Health
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    system = platform.system()

    return render_template(
        'index.html',
        uptime=uptime,
        hostname=hostname,
        status="Running",
        current_time=current_time,
        version=version,
        cpu=cpu,
        memory=memory,
        system=system
    )

@app.route('/health')
def health():
    return {"status": "OK"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)