import socket

def port_scan(ip, start_port, end_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, start_port))
    sock.close()
    return result == 0
