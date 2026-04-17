# main.py
import sys
from scanner import scan_range
from utils import validate_ip, parse_port_range

def print_results(results):
    open_ports = [p for p, open_ in results if open_]
    if open_ports:
        print("\nPorts ouverts:")
        for p in open_ports:
            print(f" - {p}")
    else:
        print("\nAucun port ouvert détecté dans la plage fournie.")
    print("\nDétail complet:")
    for port, is_open in results:
        status = "OUVERT" if is_open else "FERMÉ"
        print(f"{port:5d} : {status}")

def prompt_and_scan():
    target = input("Adresse IP cible: ").strip()
    if not validate_ip(target):
        print("Adresse IP invalide.")
        return
    pr = input("Plage de ports (ex: 20-80 ou 22): ").strip()
    try:
        start, end = parse_port_range(pr)
    except Exception as e:
        print("Plage invalide:", e)
        return
    try:
        delay = float(input("Délai entre scans en secondes (ex: 0.1) [0]: ").strip() or "0")
    except ValueError:
        print("Délai invalide, utilisation de 0.")
        delay = 0.0
    try:
        timeout = float(input("Timeout par connexion en secondes (ex: 1) [1]: ").strip() or "1")
    except ValueError:
        print("Timeout invalide, utilisation de 1.")
        timeout = 1.0

    print(f"\nScan de {target} ports {start}-{end} delay={delay}s timeout={timeout}s")
    try:
        results = scan_range(target, start, end, delay=delay, timeout=timeout)
        print_results(results)
    except KeyboardInterrupt:
        print("\nScan interrompu par l'utilisateur.")
    except Exception as e:
        print("Erreur lors du scan:", e)

def main():
    while True:
        print("\n=== Port Scanner ===")
        print("1. Lancer un scan")
        print("2. Quitter")
        choice = input("Choix: ").strip()
        if choice == '1':
            prompt_and_scan()
        elif choice == '2':
            print("Au revoir.")
            sys.exit(0)
        else:
            print("Choix invalide.")

if name == "__main__":
    main()
