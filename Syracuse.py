def syracuse(Nb:int) -> list: #Fonction syracuse
    Nb
    list = [] 
    while Nb != 1 :    
        if (Nb % 2) == 0 :  #Si le chiffre est paire
            Nb = Nb // 2
            list.append(Nb)

        else :   #Si le chiffre est impaire
            Nb = Nb * 3 + 1
            list.append(Nb)
    return list

print(syracuse(int(input("Enter a positive number : "))))