kapital = float(input("Gib das Startkapital ein"))
zinssatz = float(input("Gib den Zinssatz in Prozent ein"))
Laufzeit = int(1)

zinssatz_dezimal = zinssatz/100

einfache_zinsen = kapital*zinssatz_dezimal*Laufzeit
print(f"Die einfachen Zinsen betragen {einfache_zinsen:.2f}für 1 Jahr")

endkapital = kapital+einfache_zinsen
print(f"Das Endkapital beträgt {endkapital:.2f} nach 1 Jahr")

######################################################

rechnung_a = (120*0.07)
rechnung_b = (120+rechnung_a)
print(rechnung_b)

#######################################################

personen = int(input("Anzahl der Personen"))
aufenthaltsdauer = int(input("Anzahl der Tage"))
zimmerpreis = int(70)
nettopreis = (zimmerpreis*aufenthaltsdauer*personen)
gesamtpreis = (nettopreis*1.19)

print(f"Der Gesamtbetrag beträgt {gesamtpreis}")

########################################################

äpfel = int(input("Anzahl der Äpfel"))
bananen = int(input("Anzahl der Bananen"))
orangen = int(input("Anzahl der Orangen"))

apfel_preis = (0.5)
bananen_preis = (0.80)
orangen_preis = (0.60)

gesamtpreis = (apfel_preis*äpfel)+(bananen_preis*bananen)+(orangen_preis*orangen)
print(f"Der Gesamtpreis beträgt {gesamtpreis:.2f}")

#########################################################

