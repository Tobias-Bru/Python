#START
zahl1 = float(input("Geben sie eine Zahl ein:"))
operator = input("Geben sie den Operator ein: (+,-,*,/)")
Zahl2 = float(input("Geben sie eine zweite Zahl ein:"))

if operator == '+':
    ergebnis = zahl1 + Zahl2
    print(f"Das Ergebnis ist: {ergebnis}")
elif operator == '-':
    ergebnis = zahl1 - Zahl2
    print(f"Das Ergebnis ist: {ergebnis}")
elif operator == '*':
    ergebnis = zahl1 * Zahl2
    print(f"Das Ergebnis ist: {ergebnis}")
elif operator == '/':
    ergebnis = zahl1 / Zahl2
    print(f"Das Ergebnis ist: {ergebnis}")

#ENDE