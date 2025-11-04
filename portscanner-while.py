import socket
import sys

def check_port(hostIp, port):
    """
    Prüft einen einzelnen Port auf einem bereits aufgelösten Host.
    Gibt nur aus, wenn der Port offen ist.
    """
    # Erstelle ein neues Socket-Objekt für jeden Port (wichtig für Threading später)
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.settimeout(1)  # Zeitlimit von 1 Sekunde

    try:
        # connect_ex gibt 0 zurück, wenn die Verbindung erfolgreich war
        result = mySocket.connect_ex((hostIp, port))
        
        if result == 0:
            print(f"Port {port} ist offen.")
        # 'else' wird weggelassen, um geschlossene Ports nicht anzuzeigen
            
    except socket.error:
        # Falls ein Verbindungsfehler auftritt, Port als geschlossen behandeln
        pass
    finally:
        mySocket.close()


# Hauptprogramm-Block
if __name__ == "__main__":
    
    hostInput = input("Bitte Host-IP-Adresse oder Domain eingeben: ")
    
    try:
        # Hostnamen *einmal* vor der Schleife auflösen
        try:
            hostIp = socket.gethostbyname(hostInput)
        except socket.gaierror:
            print(f"Hostname-Fehler: Konnte '{hostInput}' nicht auflösen.")
            sys.exit()

        # Port-Bereich abfragen
        startPort_str = input(f"Bitte Start-Port eingeben (z.B., 1): ")
        endPort_str = input(f"Bitte End-Port eingeben (z.B., 1024): ")

        startPort = int(startPort_str)
        endPort = int(endPort_str)

        # Eingaben validieren
        if not (0 < startPort <= 65535 and 0 < endPort <= 65535 and startPort <= endPort):
            raise ValueError("Ports müssen zwischen 1 und 65535 liegen und Start-Port <= End-Port sein.")

        print(f"\nStarte Scan für {hostInput} (IP: {hostIp}) von Port {startPort} bis {endPort}...")
        print("-" * 40) # Trennlinie

        # --- Hier ist die while-Schleife ---
        currentPort = startPort
        
        while currentPort <= endPort:
            check_port(hostIp, currentPort)
            currentPort += 1  # WICHTIG: Port für den nächsten Durchlauf erhöhen
        # --- Ende der while-Schleife ---

        print("-" * 40)
        print("Scan abgeschlossen.")

    except ValueError as ve:
        print(f"Fehler: Ungültige Port-Eingabe. {ve}")
    except KeyboardInterrupt:
        print("\nOperation vom Benutzer abgebrochen.")
        sys.exit()
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        sys.exit()