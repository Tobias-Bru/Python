

äpfel = int(input("Anzahl der Äpfel"))
bananen = int(input("Anzahl der Bananen"))
orangen = int(input("Anzahl der Orangen"))

apfel_preis = (0.5)
bananen_preis = (0.80)
orangen_preis = (0.60)

gesamtpreis = (apfel_preis*äpfel)+(bananen_preis*bananen)+(orangen_preis*orangen)
print(f"Der Gesamtpreis beträgt {gesamtpreis:.2f}")