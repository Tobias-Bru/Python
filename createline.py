#def createline(n):
#
#    return '*' * n
#n = int(input("How many stars do you want to print"))
#print(createline(n))

#####################################

#def createline(Length:int)->str:
#    line = ""
#    for i in range(Length):
#        line += "*"
#
#    print(line)
#
#input_length = input("Please enter line length")
#
#
#createline(int(input_length))

#######################################

#def starline():
#    sterne = int(input("Gib eine Zahl ein: "))
#    temp = 0
#    final = ""
#    while temp < sterne:
#        if temp % 2 == 0:
#            final = final + "*"
#        else:
#            final = final + "-"
#        temp = temp +1
#    print(final)
#
#starline()

##########################################

#reihen = int(input("Wie viele Reihen? "))
#i = 1
# 
#while i <= reihen:
#    print('*' * i)
#    #print('-' * i)
#    i += 1

############################################

#def stern(zeilen):
#    i = 1
#    while i <= zeilen:
#        print("*" * i)
#        i = i + 1
#
#    #stern(5)
#
#def sterne(lines):
#    i = 1
#    while i <= lines:
#        if i % 2 == 0:
#            print("-" * i)
#        else:
#            print("*" * i)
#        i += 1
#
#sterne(6)

################################################

#Sternendreieck

#def erstelle_stern_liste(zeilen_anzahl):
#    stern_liste = []
#    i = 1
#    while i <= zeilen_anzahl:
#        aktuelle_zeile = '*' * i
#        stern_liste.append(aktuelle_zeile)
#        i = i + 1 
#    return stern_liste
#
#def drucke_liste(element_liste):
#    print("\n--- Ihr Dreieck ---")    
#    for element in element_liste:
#        print(element)
#
#def main():
#    print("--- Sternen-Dreieck ---")
#    try:
#        eingabe_text = input("Wie viele Zeilen sollen gedruckt werden? ")
#        anzahl = int(eingabe_text)
#        if anzahl > 0:
#            meine_stern_liste = erstelle_stern_liste(anzahl)            
#            drucke_liste(meine_stern_liste)
#            print(f"\n(Das Array im Hintergrund war: {meine_stern_liste})")
#        else:
#            print("Eingabe ungültig: Bitte nur eine Zahl größer als 0 eingeben.")
#    except ValueError:
#        print(f"Fehler: '{eingabe_text}' ist keine gültige *Zahl*.")
#if __name__ == "__main__":
#    main()


#Sternen-Dreieck umgekehrt

def erstelle_stern_liste_umgekehrt(zeilen_anzahl):
    stern_liste = []
    i = zeilen_anzahl
    
    while i > 0:
        aktuelle_zeile = '*' * i
        stern_liste.append(aktuelle_zeile)
        i = i - 1
    return stern_liste


def drucke_liste(element_liste):
    print("\n--- Ihr umgekehrtes Dreieck ---") 
    for element in element_liste:
        print(element)

def main():
    print("--- Sternen-Dreieck (Umgekehrt) ---")
    try:
        eingabe_text = input("Wie viele Zeilen sollen gedruckt werden? ")
        anzahl = int(eingabe_text)
        if anzahl > 0:
            meine_stern_liste = erstelle_stern_liste_umgekehrt(anzahl)
            drucke_liste(meine_stern_liste)
            print(f"\n(Das Array im Hintergrund war: {meine_stern_liste})")
        else:
            print("Eingabe ungültig: Bitte nur eine Zahl größer als 0 eingeben.")
    except ValueError:
        print(f"Fehler: '{eingabe_text}' ist keine gültige *Zahl*.")
if __name__ == "__main__":
    main()


