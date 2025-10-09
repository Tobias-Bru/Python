#implementation Cesar Encryption

ALPHABET = [
    ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


#this function does encryption
def encrypt()->str:
    klar_text = input("\nplease enter a Text to encrypt:")
    key = input("please enter encryption key:")
    key = int(key)
    for character in klar_text:
        alphabet_index = ALPHABET.index(character)
        print(f"\n {character}")
        print(f"index position in kunde text for Alphabet is:" + str(alphabet_index))
        new_char_index = ALPHABET.index(character)+int(key)
        encryptedChar = ALPHABET[new_char_index]
        print(f"das ist encrypted:  " + encryptedChar)
    return "it is encrypted from" + klar_text + "and Key" + key

def decode()->str:
    cypherText = input("\nplease enter a Text to decrypt")
    key = input("please enter DECRYPTION KEY")
    return "it is decrypted from " + cypherText + "and Key:" + key




def main():
    result = ""
    print("hello, i am cesar enc and dec app!")
    userChoice = input("if you want to decrypt, press d, if you want to encrypt press e")
    
    if(userChoice == "e"):
        result = encrypt()
    elif userChoice== "d":
        result = decode()
    else:
        result = "you must enter only e or d"
    
    print(result)

if __name__ == "__main__":
    main()