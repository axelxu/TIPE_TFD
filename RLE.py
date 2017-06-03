## Pour les textes

def RLE(chaine): # En O(n), marche bien pour du texte mais pas pour des chaines de chiffres car il peut y avoir ambiguité
    i = 0
    res = ""
    n = len(chaine)
    while i< n:
        x = chaine[i]
        c = 1
        while i+c < n and chaine[i+c] == x:
            c += 1
        if c == 1:
            res = res + x
            i = i+1
        else:
            res = res + str(c) + x
            i = i+c
    return res    


def RLE_inverse(chaine):    # En O(n)
    i = 0
    res = ""
    n = len(chaine)
    while i<n:
        if ord(chaine[i]) >= 48 and ord(chaine[i]) <= 57: # si c'est un entier entre 0 et 9
            c = 1
            nb = int(chaine[i])
            while i+c < n and ord(chaine[i+c]) >= 48 and ord(chaine[i+c]) <= 57: # on regarde s'il y a un nombre à plusieurs chiffres
                nb = 10*nb + int(chaine[i+c])
                c += 1
            for k in range(nb):
                res = res + chaine[i+c]
            i = i + c + 1
        else:
            res = res + chaine[i]
            i += 1
    return res



## Pour les images

def RLE_chiffres(chaine):   # En O(n)
    i=0
    res = ""
    n=len(chaine)
    l = ["a","b","c","d","e","f","g","h","i","k"]
    while i < n:
        x = chaine[i]
        c = 1
        while i+c < n and chaine[i+c] == x:
            c += 1
        if c == 1:
            res = res + l[int(x)]
            i += 1
        else:
            res = res + str(c) + l[int(x)]
            i = i+ c
    return res
            
    
def RLE_chiffres_inverse(chaine):  # En O(n)
    i = 0
    res = ""
    n = len(chaine)
    while i<n:
        if ord(chaine[i]) >= 48 and ord(chaine[i]) <= 57: # si c'est un entier entre 0 et 9
            c = 1
            nb = int(chaine[i])
            while i+c < n and ord(chaine[i+c]) >= 48 and ord(chaine[i+c]) <= 57: # on regarde s'il y a un nombre à plusieurs chiffres
                nb = 10*nb + int(chaine[i+c])
                c += 1
            for k in range(nb):
                res = res + str( ord(chaine[i+c]) - 97) # 97 est l'ord de a
            i = i + c + 1
        else:
            res = res + str( ord(chaine[i]) - 97)
            i += 1
    return res
    
    
    
    
    