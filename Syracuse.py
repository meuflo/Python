def syracuse(Nb:int) -> list: #Syracuse function
    Nb
    list = [] 
    while Nb != 1 :    
        if (Nb % 2) == 0 :  #If the number is even
            Nb = Nb // 2
            list.append(Nb)

        else :   #If the number is odd
            Nb = Nb * 3 + 1
            list.append(Nb)
    return list

print(syracuse(int(input("Enter a positive number : "))))
