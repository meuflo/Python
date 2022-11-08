def anagramme(x,y): #Fonction qui définit si les mots sont des anagrammes.
    if sorted(x) == sorted(y):
        return True
    else:
        return False


a = input("Saisir le premier mot : ")
b = input("Saisir le deuxieme mot : ")

tab = [a,b]
tab1 = { 'éèêẽë' : 'e'     #Tableau de référencement des lettres a remplacer
        , 'ç'    : 'c'
        , 'àâãâäåá'  : 'a'
        , 'ùúûü'    : 'u'
        , 'îíìï' : 'i'
        , 'óòôöõø' : 'o'
        }

x = a.lower()
y = b.lower()
print(a)
print(b)

word_without_accent = "" #Traitement des valeurs avec accent
for i in x :
    for k in tab1:
        if i in k: 
            i = tab1[k] 
            break
    word_without_accent += i
    x = word_without_accent

word_without_accent = ""
for i in y :
    for k in tab1:
        if i in k: 
            i = tab1[k] 
            break
    word_without_accent += i
    y = word_without_accent

print(anagramme(x,y))

