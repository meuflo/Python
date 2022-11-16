from random import *

#tab = [35, 166.5, 13, 94, -7, 43.4, 70, 2] #Si on utilise pas la génération aléatoire
tab = [randint(-100,500) for i in range(10)] #Génération aléatoire

def sort_selection(tab) : #Trouver le nombre mini
   for i in range(len(tab)) :     
       min = i
       for j in range(i+1, len(tab)) : 
           if tab[min] > tab[j] :
               min = j
                
       vp = tab[i] #Inverse la position des nombres dans la liste (valeur temporaire, vp = value to be processed)
       tab[i] = tab[min]
       tab[min] = vp

   return tab
 
sort_selection(tab)
 
print ("The sorting table is : ")
for i in range(len(tab)) : #Génération de la liste croissante
    print(tab[i])