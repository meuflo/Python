def encrypt(text,key): #Encryption function
    result = ""
    for i in range(len(text)):
        char=text[i]
        result+= chr((ord(char) + key - 96) % 26 + 96)
    return result                                        

def decrypt(text,key): #Decryption function
    result = ""
    for i in range(len(text)):
        char=text[i]
        result+= chr((ord(char) - key - 96) % 26 + 96)
    return result
    
    
def menu() : #Menu function
    print("[1] Encrypt")
    print("[2] Decrypt")
    print("[0] Leave")
    
menu()
option = int(input("Choix : "))

while option != 0 : 
    if option == 1: #Encryption
        text = input("Enter a word : ")
        key = int(input("Enter a key : "))
        print(encrypt(text,key))
        break
    
    elif option == 2 : #Decryption
        text = input("Enter a word : ")
        key = int(input("Enter a key : "))
        print(decrypt(text,key))
        break
