zimmerpreis=float(input("Geben Sie den Zimmerpreis pro Person und Nacht ein: "))
aufenthaltsdauer=int(input("Geben Sie die Aufenthaltsdauer in Nächten ein: "))
alter_kind=int(input("Gebe bitte das alter des Kindes ein: "))
rabatt=0
kinderpreis=0

if alter_kind<7:
    rabatt=100
else:
    rabatt=70

kinderpreis=zimmerpreis*aufenthaltsdauer*(1-rabatt/100)
erwachsenenpreis=2*zimmerpreis*aufenthaltsdauer

gesamtpreis=erwachsenenpreis+kinderpreis

print(f"Gesamtpreis für die Familie beträgt: {gesamtpreis:.2f}")

#################################################################

import random

print("Geben sie eine Zahl zwischen 1 bis 5 ein: ")
input_value=input()

if input_value.isdigit(): #isdigit fängt valueerror ab
    input_value=int(input_value)
    zufallszahlgenerator=random.randint(1,5)
    if input_value==zufallszahlgenerator:
        print("Herzlichen Glückwunsch du hast gewonnen")
    else:
        print(f"Schade sie haben verloren, die korrekte Zahl war {zufallszahlgenerator}")
else:
    print("Du hast keinen String eingegeben das aussieht wie eine Zahl")

print("Danke das du gespielt hast")

#####################################################################

star_wars=["Meister Klink","Yoda","Darth Vader","Leia Organa","Han Solo","Luke Skywalker","Mace Windu","Jar Jar Binks"]

print("Darth Vader" in star_wars)

if "Darth Vader" in star_wars:
    print("Ja er ist ein Bösewicht aber ändert seine Meinung")
else:
    print("Wahrscheinlich ein Buchstabenfehler?")

if "Herr Cakir" in star_wars:
    print("Das wäre ja mal genial")
else:
    print("schade er ist nicht dabei")

##########################################################################

text="Ich bin ein Berliner"

if "ein" in text:
    print("Ja es gibt ein ein")
else:
    print("Es gibt kein ein")

##########################################################################

alter=30

if not alter >=30:
    print("Ja ich bin nicht über 31")
else:
    print("Ich bin über 30")

############################################################################

umschueler=["Enton","Glumanda","Glurak","Glutexo","Shiggy"]

if "Mewtwo" not in umschueler:
    print("Schade Mewtwo ist nicht dabei")

if not "Mewtwo" in umschueler: #schlechte Variante
    print("nope MEWTWO ist nicht dabei")

##############################################################################

start=0

while start <5:
    print(start)
    #0      0   1
    #start=start+1                   #alternativ            + = inkrementieren      - = dekrementieren
    start+=1
    print("geht weiter")
print("ende")

################################################################################

zimmerpreis=float(input("Geben sie bitte den Zimmerpreis für heute ein: "))
aufenthaltsdauer=float(input("Geben sie bitte die Dauer ein: "))
anzahl_kinder=int(input("Wieviele Kinder hat die Familie zum einchecken: "))

kinderpreis=0.0
zaehler=0

while zaehler <anzahl_kinder: #zähle ich gleich runter und zaehler 0
    alter_kind=int(input(f"Gebe jetzt bitte an wie alt Kind {zaehler+1} ist"))

    if alter_kind <=6:
        rabatt=100
    else:
        rabatt=50
    
    kinderpreis=zimmerpreis*aufenthaltsdauer*(1-rabatt/100)
    zaehler+=1

erwachsenenpreis=2*zimmerpreis*aufenthaltsdauer
gesamtpreis=erwachsenenpreis+kinderpreis

print("Angebot")
print(f"\n Zimmerpreis Nacht und Person {zimmerpreis} € und Aufenthaltsdauer {aufenthaltsdauer} in Nächte und Preis {gesamtpreis:.2f}")

#####################################################################################

