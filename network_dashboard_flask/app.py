from flask import Flask, render_template, request
from dns_lookup import dns_lookup
from ping_test import ping_host
from port_scanner import port_scan
from http_server import run_server
from proxy_server import proxy_server
import threading
from ip2geotools.databases.noncommercial import DbIpCity # Added for GeoIP

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        action = request.form.get("action")

        if action == "dns":
            domain = request.form["dns_domain"]
            result = dns_lookup(domain)

        elif action == "ping":
            host = request.form["ping_host"]
            if ping_host(host):
                result = f"{host} is reachable"
            else:
                result = f"{host} is unreachable"

        elif action == "scan":
            ip = request.form["scan_ip"]
            start_port = int(request.form["start_port"])
            end_port = int(request.form["end_port"])
            result = f"Scanning {ip} from port {start_port} to {end_port}...\n"
            open_ports = []
            for port in range(start_port, end_port + 1):
                try:
                    if port_scan(ip, port, port):
                        open_ports.append(port)
                except:
                    continue
            result += f"Open ports: {open_ports}"

        elif action == "http":
            port = int(request.form["http_port"])
            threading.Thread(target=run_server, args=(port,), daemon=True).start()
            result = f"HTTP server started on port {port}"

        elif action == "proxy":
            remote = request.form["proxy_remote"]
            threading.Thread(target=proxy_server, args=('127.0.0.1', 8080, remote, 80, True), daemon=True).start()
            result = f"Proxy started on 127.0.0.1:8080 → {remote}:80"

        elif action == "geoip": # New GeoIP action
            ip = request.form["geoip_ip"]
            try:
                response = DbIpCity.get(ip, api_key="free")
                result = (
                    f"IP: {response.ip}\n"
                    f"City: {response.city}\n"
                    f"Region: {response.region}\n"
                    f"Country: {response.country}\n"
                    f"Latitude: {response.latitude}\n"
                    f"Longitude: {response.longitude}\n"
                )
            except Exception as e:
                result = f"Error: {str(e)}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)