def anagramme(x,y): #Function that defines if the words are anagrams
    if sorted(x) == sorted(y):
        return True
    else:
        return False


a = input("Enter the first word : ")
b = input("Enter the second word : ")

tab = [a,b]
tab1 = { 'éèêẽë' : 'e'    #Reference table of letters to replace
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

word_without_accent = "" #Treatment of values with emphasis
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

