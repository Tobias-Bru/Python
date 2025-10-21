#start
strompreis = 0.4

verbrauch_tv = 3*1*3*365
verbrauch_herd = 4*2*2*52
verbrauch_router = 2*4*365
verbrauch_heizung = 8*20*170

gesamtverbrauch = verbrauch_tv+verbrauch_herd+verbrauch_router+verbrauch_heizung

gesamtkosten = strompreis*gesamtverbrauch

print(f"Gesamtverbrauch im Jahr beträgt {gesamtkosten:.2f}") # .2f sind die Nachkommastellen
#print(10/2)
#print("Das Ergebnis lautet ",gesamtkosten)
#print(f"{10/2} ich kann auch direkt {gesamtkosten} {strompreis/gesamtverbrauch}")
#print("Das Ergebnis von"#str(gesamtverbrauch))

#end

a = "7" #string
b = "5"

print(a+b)
print(int(a)+int(b)) #konvertiert oder parsing

a = "3.5"
b = "2.9"

ergebnis = float(a)/float(b)

print(float(a)/float(b))
print(f"{float(ergebnis):.2f}")




####

studenten = "Jörg,Patrick,Holger,Christopher,Christian" # Mit [Liste] den Klammer eine Liste erstellen
ergebnis = studenten.split(",") #Leerzeichen trennt die Liste mit einem Kommata. Tennen mit ","
print(ergebnis)
print(type(ergebnis)) # Was für ein Datentyp es ist
#ausgabe = ",  ".join(studenten)

#join = joined ein Text als eine Liste
#split = Leerzeichen trennt die Liste mit einem Kommata, wo ein Leerzeichen ist. Kommata "," trennt...
#array = liste
####



