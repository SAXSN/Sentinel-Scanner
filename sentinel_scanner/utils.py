import socket

def resolve_host(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        return None
