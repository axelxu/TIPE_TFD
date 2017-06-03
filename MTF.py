def MtF(chaine): # En O(taille de la chaine) car la liste l est de taille constante. Attention à n'utiliser que des caracteres ASCII
    l = [chr(i) for i in range(32,127)] # tous les caracteres ASCII
    res = ""
    for x in chaine:
        indice = 0
        if x != '\\': # génant pour les textes importés
            while l[indice] != x:
                indice += 1
            res = res + chr(indice+32) # les 31 premiers caracteres ASCII sont des caracteres speciaux
            l.remove(x)
            l = [x] + l
    return res
    


def MtF_inverse(chaine):    # En O(taille de la chaine) 
    l = [chr(i) for i in range(32,127)]
    res = ""
    for x in chaine:
        res = res + l[ord(x) - 32]
        a = l[ord(x) - 32]
        del l[ord(x) - 32]
        l = [a] + l
    return res   

