from random import randint

print("Willkommen bei THE SAW, bei dem tödlichen recht logischen Zahlenrätsel.....")
print("Du hast 5 Versuche, die richtige Zahl zwischen 1 und 10 zu erraten")
print("Wen du es nicht schaffst, wirst du auf die grausamste Weise was ein Autor sich ausdenken kann elimiert \U0001F608")

random_number=randint(1,10)
attempts=5

while attempts>0:
    input_value=input(f"Gebe eine Zahl zwischen 1 und 10 ein, du hast aktuell {attempts} Versuche frei ")

    if input_value.isdigit():
        input_value=int(input_value)
        if 1<= input_value <=10:
            if input_value==random_number:
                print("---------------------------------------------------------")
                print("\n Du hast gewonnen! Du darfst ab heute weiterleben es sei denn es gibt eine andere Folge. Hier bekommst nen Döner \U0001F60A")
                print("----------------------------------------------------------")
                break
            else:
                attempts-=1
                if attempts>0:
                    print(" Falsch geraten, versuche es nochmal \U0001F608 ")
                else:
                    print("-------------------------------------------")
                    print("Du hast jetzt alle deine Chancen verspielt")
                    print("Verabschiede dich schon mal von deinem Elend für dich ist Game Over \U0001F480 ")
                    print(f"Die Lösung des Rätsels war {random_number}")
        else:
            print("Die REgeln lauten Zahlen zwischen 1 und 10 eingeben \U0001F608 ")
    else:
        print("Zahlen sehen anders aus!!!!!!")
        attempts-=1
print("Das Todespiel hat mir persönlich Spaß bereitet")