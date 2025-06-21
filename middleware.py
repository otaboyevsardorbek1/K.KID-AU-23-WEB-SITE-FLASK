from flask import request, abort
from datetime import datetime
import os

# Blacklistlar
blacklisted_agents = ['curl', 'bot', 'python', 'scrapy', 'httpclient']
blacklisted_ips = ['192.168.1.100', '10.10.10.10']  # Misol uchun

# Botni aniqlash
def is_bot(user_agent, ip):
    for bad in blacklisted_agents:
        if bad in user_agent.lower():
            return True
    if ip in blacklisted_ips:
        return True
    return False

# before_request function
def block_bots(app):
    @app.before_request
    def check_for_bots():
        ip = request.remote_addr
        ua = request.headers.get("User-Agent", "")
        if is_bot(ua, ip):
            # Log qilish
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            os.makedirs("logs", exist_ok=True)
            with open("logs/user_log.txt", "a") as f:
                f.write(f"{now} | BLOCKED | IP: {ip} | Agent: {ua}\n")
            abort(403)
