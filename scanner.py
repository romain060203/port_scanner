# scanner.py
import socket
import time


def scan_port(target, port, timeout=1.0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        return result == 0


def scan_ports(target, start_port, end_port, timeout=1.0, delay=0.05):
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port, timeout):
            open_ports.append(port)
        time.sleep(delay)

    return open_ports
