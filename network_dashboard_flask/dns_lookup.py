import socket

def dns_lookup(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return f"The IP address of {domain_name} is: {ip_address}"
    except socket.gaierror as e:
        return f"Error: {e}"
