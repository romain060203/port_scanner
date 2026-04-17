# utils.py
import ipaddress
from typing import Tuple

def validate_ip(ip_str: str) -> bool:
    """Valide une adresse IPv4 ou IPv6."""
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def parse_port_range(range_str: str) -> Tuple[int, int]:
    """
    Parse '20-80' ou '22' et retourne (start, end).
    Lève ValueError si invalide.
    """
    if '-' in range_str:
        parts = range_str.split('-', 1)
        if len(parts) != 2:
            raise ValueError("Format de plage invalide.")
        start = int(parts[0].strip())
        end = int(parts[1].strip())
    else:
        start = end = int(range_str.strip())
    if start < 1 or end > 65535 or start > end:
        raise ValueError("Plage de ports invalide. Doit être entre 1 et 65535 et start <= end.")
    return start, end
