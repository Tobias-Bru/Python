a=10
b=2
c=a/b #Division

c=a*b #Multiplikation
c=a+b #Addition
c=a-b #Subtraktion

c=a%b #Modulo 0, gibt den Restwert zurück, 10 geteilt durh 2 ist 5 mit Rest 0

print(c)#Ausgabe alles was im Terminal erscheinen soll
# alles was in () steht nennt man Funktion, eine Funktion tut etwas

print(10/2) #Alternative
print(f"{a/b}") #Alternative
print("Das Ergebnis ist:", a/b) #Alternative
print("Das Ergebnis" +str(a)+ "und" +str(b)+ "ergibt" +str(c)) #nicht empfohlen
print(f"Das Ergebnis von {a} und {b} ist {c}") #f-string String Literale



#           0       1       2       3           Reihenfolge für pop
schueler=["Name0","Name1","Name2","Name3"]

schueler.pop() #letzten Eintrag löschen in der Liste ohne Wert
schueler.append("NeuerName") # fügt der Liste einen Namen am Ende hinzu

print(schueler)
print(len(schueler)) #gibt die Länger der Liste zurück
print(schueler[2]) #gibt den Eintrag ander Stelle 2 zurück


a=2
b=3

istkorrekt=a>b #entweder true oder false
print(istkorrekt)