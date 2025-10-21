#in the following code problem solving is to calculate the exact full number per person
#the 500 cannot be devided to 3, we have float, but we want to calculate full numbers

Geld = 500
Name1 = 166
Name2 = 166
Name3 = 166
Rest = Geld % 3    #modulu Ergebnis 2
teilbaresGeld = Geld - Rest #Ergebnis 498
Name1 = teilbaresGeld/3
print(f"Geld von Name1: " + str(Name1))