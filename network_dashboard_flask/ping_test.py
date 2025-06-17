import os
import platform

def ping_host(host):
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    response = os.system(f"ping {ping_str} {host} > nul 2>&1")
    return response == 0
