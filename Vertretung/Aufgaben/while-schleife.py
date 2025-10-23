#START
#Aufgabe 1 Zähle von 1 bis 10

Zahl = 0

while Zahl <=10:
    print(Zahl)
    Zahl+=1
print("Ende")


#Aufgabe 2 While-Schleife II Einfache Passwortprüfung

passwort =  "passwort123"
attempts = 3

print("Bitte gebe das Passwort ein: ")

while attempts>0:
    eingabe_passwort = input()

    if eingabe_passwort==passwort:
        print("Das Passwort war erfolgreich!")
        break
    else:
        print("Falsches Passwort!")
        attempts-=1
