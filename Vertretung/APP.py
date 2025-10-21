print("Bitte trage deinen Benutzernamen ein: ")
username=input()

print("Bitte gebe dein Passwort ein: ")
passwort=input()

print("Registrierung erfolgreich!")
print("-----------------------------")

#Login
print("Gebe deinen Benutzernamen ein")
eingabe_username=input()

if eingabe_username==username:
    print("Nutzername korrekt, gebe dein Passwort ein: ")
    eingabe_passwort=input()
    if eingabe_passwort==passwort:
        print("Login erfolgreich!")
    else:
        print("Falsches Passwort!")
else:
    print("Falscher Benutzername!")