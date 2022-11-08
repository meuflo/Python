def encrypt(text,key):
    result = ""
    for i in range(len(text)):
        char=text[i]
        result+= chr((ord(char) + key - 96) % 26 + 96)  #ord permet de convertir le mot en nombre (table ascii), chr fait l'inverse
    return result                                       #ascii : a = 97 mais a = 0 donc on commence a 96 

def decrypt(text,key):
    result = ""
    for i in range(len(text)):
        char=text[i]
        result+= chr((ord(char) - ke    y - 96) % 26 + 96)
    return result
    
    
def menu() : #Menu principal
    print("[1] Encrypt")
    print("[2] Decrypt")
    print("[0] Quitter")
    
menu()
option = int(input("Choix : "))

while option != 0 : 
    if option == 1:
        text = input("Enter a word : ")
        key = int(input("Enter a key : "))
        print(encrypt(text,key))
        break
    
    elif option == 2 : 
        text = input("Enter a word : ")
        key = int(input("Enter a key : "))
        print(decrypt(text,key))
        break