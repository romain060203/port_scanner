# scanner.py
import socket
import time
from typing import List, Tuple

DEFAULT_TIMEOUT = 1.0

def scan_port(host: str, port: int, timeout: float = DEFAULT_TIMEOUT) -> bool:
    """Retourne True si le port est ouvert."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return result == 0
    except Exception:
        return False

def scan_range(host: str, start_port: int, end_port: int, delay: float = 0.0,
               timeout: float = DEFAULT_TIMEOUT) -> List[Tuple[int, bool]]:
    """
    Scanne les ports de start_port à end_port inclus.
    Retourne une liste de tuples (port, is_open).
    """
    results = []
    for port in range(start_port, end_port + 1):
        is_open = scan_port(host, port, timeout=timeout)
        results.append((port, is_open))
        if delay > 0:
            time.sleep(delay)
    return results
