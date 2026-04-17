# main.py
import sys
from scanner import scan_ports
from utils import validate_ip, validate_port, ask_yes_no

def get_positive_float(prompt, default):
    value = input(prompt).strip()
    if value == "":
        return default
    try:
        number = float(value)
        if number <= 0:
            raise ValueError
        return number
    except ValueError:
        print("Valeur invalide, utilisation de la valeur par défaut.")
        return default

def main():
    print("=== PORT SCANNER ===")
    print("Utilise cet outil uniquement sur des machines locales ou autorisées.\n")

    if not ask_yes_no("Confirmez-vous avoir l'autorisation de scanner cette cible ?"):
        print("Scan annulé.")
        sys.exit(0)

    target = input("Adresse IP cible : ").strip()
    if not validate_ip(target):
        print("Erreur : adresse IP invalide.")
        sys.exit(1)

    start_port = input("Port de début : ").strip()
    end_port = input("Port de fin : ").strip()

    if not validate_port(start_port) or not validate_port(end_port):
        print("Erreur : ports invalides.")
        sys.exit(1)

    start_port = int(start_port)
    end_port = int(end_port)

    if start_port > end_port:
        print("Erreur : le port de début doit être inférieur ou égal au port de fin.")
        sys.exit(1)

    timeout = get_positive_float("Timeout en secondes [1.0] : ", 1.0)
    delay = get_positive_float("Délai entre les scans en secondes [0.05] : ", 0.05)

    print(f"\nScan de {target} sur les ports {start_port}-{end_port}...\n")

    try:
        open_ports = scan_ports(target, start_port, end_port, timeout=timeout, delay=delay)

        if open_ports:
            print("Ports ouverts détectés :")
            for port in open_ports:
                print(f"- {port}")
        else:
            print("Aucun port ouvert détecté.")

    except KeyboardInterrupt:
        print("\nScan interrompu par l'utilisateur.")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        sys.exit(1)
        
if name == "__main__":
    main()
