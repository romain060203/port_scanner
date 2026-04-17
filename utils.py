# utils.py
import ipaddress


def validate_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def validate_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False


def ask_yes_no(message):
    answer = input(f"{message} (o/n) : ").strip().lower()
    return answer == "o"
