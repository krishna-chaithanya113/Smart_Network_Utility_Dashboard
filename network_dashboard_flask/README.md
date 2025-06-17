# 🌐 Smart Network Utility Dashboard

A powerful and beginner-friendly **Flask-based web application** for performing essential network operations like DNS lookup, Ping tests, Port scanning, running an HTTP server, launching a proxy server, and locating the geographic position of an IP using GeoIP.

> 🔧 Developed using Python, Flask, and basic networking libraries. Ideal for students, interns, and enthusiasts working on Computer Networks or Cybersecurity projects.

---

## 🚀 Features

- 🔍 **DNS Lookup**: Resolve domain names into IP addresses.
- 🏓 **Ping Test**: Test host/network reachability.
- 🔐 **Port Scanner**: Scan a range of TCP ports on a target IP.
- 🌐 **GeoIP Locator**: Get country, region, and city for any public IP.
- 🖥️ **HTTP Server**: Launch a local web server to serve simple HTML.
- 🔁 **Proxy Server**: Forward traffic from your machine to a remote host.

---

## 🖼️ User Interface

Built with a modern, responsive HTML UI using inline CSS. Interact through your web browser.

![screenshot](https://via.placeholder.com/600x300?text=Smart+Network+Utility+Dashboard)

---

## 📂 Project Structure

```
network_dashboard/
├── app.py                  # Flask application controller
├── dns_lookup.py           # DNS resolution logic
├── ping_test.py            # Host ping function
├── port_scanner.py         # TCP port scanning logic
├── proxy_server.py         # Proxy server implementation
├── http_server.py          # HTTP server module
├── templates/
│   └── index.html          # Frontend UI template (HTML)
├── static/
│   └── style.css           # Custom UI styling (optional)
```

---

## ⚙️ Installation & Setup

### 🔧 Prerequisites

- Python 3.x
- pip

### 📦 Install Dependencies

```bash
pip install flask ip2geotools
```

### ▶️ Run the App

```bash
python app.py
```

### 🌍 Open in Browser

Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Sample Outputs

### DNS Lookup
```
Input: google.com
Output: The IP address of google.com is: 142.250.xxx.xxx
```

### Ping Test
```
Input: 8.8.8.8
Output: 8.8.8.8 is reachable
```

### Port Scanner
```
Input: 127.0.0.1 (Ports 70-90)
Output: Open ports: [80]
```

### GeoIP Locator
```
Input: 8.8.8.8
Output:
  City: Mountain View
  Region: California
  Country: US
  Latitude: 37.4056
  Longitude: -122.0775
```

---

## 🛡️ Disclaimer

- This tool is for **educational and ethical** purposes only.
- Do **not** scan or probe networks you do not own or have permission to test.

---

## 🧑‍💻 Authors

- Uday Kiran  
- Team: S. Hasika,  R. Sidhartha Chowdary, N. Chaitanya 
- 💡 Guided by: [Instructor/Institution Name Here]

---

## 📜 License

MIT License — free to use, share, and modify with attribution.
