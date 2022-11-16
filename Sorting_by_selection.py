from random import *

#tab = [35, 166.5, 13, 94, -7, 43.4, 70, 2] #If we do not use random generation
tab = [randint(-100,500) for i in range(10)] #Random generation

def sort_selection(tab) : #Find the minimum number
   for i in range(len(tab)) :     
       min = i
       for j in range(i+1, len(tab)) : 
           if tab[min] > tab[j] :
               min = j
                
       vp = tab[i] #Invert the position of the numbers in the list
       tab[i] = tab[min]
       tab[min] = vp

   return tab
 
sort_selection(tab)
 
print ("The sorting table is : ")
for i in range(len(tab)) : #Generation of the growing list
    print(tab[i])
