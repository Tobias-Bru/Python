# Start

items = ["Laptop", "Maus", "Tastatur", "Monitor", "Grafikkarte", "Soundkarte", "Netzwerkkarte", "Netzteil", "USB-Hub", "External-SSD"]

print("--- Verfügbare Items ---")
for i, item in enumerate(items):
    print(f"{i + 1}: {item}")
print("-------------------------")

try:
    auswahl_str = input("Welches Item soll geliefert werden? (Bitte Nummer eingeben): ")
    item_nummer = int(auswahl_str)

    index_zum_loeschen = item_nummer - 1

    if 0 <= index_zum_loeschen < len(items):
        entferntes_item = items.pop(index_zum_loeschen)
        
        print(f"'{entferntes_item}' wird versendet.")
        
        print("Danke!")

    else:
        print(f"Fehler: Nummer {item_nummer} ist nicht in der Liste.")

except ValueError:
    print("Fehler: Das war keine gültige Zahl.")

print("\n--- Verbleibende Items ---")
print(items)

# Ende