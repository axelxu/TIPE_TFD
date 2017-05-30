from cmath import exp
from cmath import pi
import numpy as np
import matplotlib.pyplot as plt 
m=[[140,144,147,140,140,155,179,175],[144,152,140,147,140,148,167,179],[152,155,136,167,163,162,152,172],[168,145,156,160,152,155,136,160],[162,148,156,148,140,136,147,162],[147,167,140,155,155,140,136,162],[136,156,123,167,162,144,140,147],[148,155,136,155,152,147,147,136]]
## transformation d'un matrice 8*8 en sa TCD
def c(i) :
    if i == 0 :
        return(1/np.sqrt(2))
    else :
        return(1)    
    
    
    
def tcd(mat) :
    passage=[np.zeros(8) for i in range(8)]
    mattcd=[np.zeros(8) for i in range(8)]    
    for i in range(8) :
        for j in range(8) :
            passage[i][j] = c(j)*(np.sqrt(2/8))*np.cos(((2*i+1)*j*np.pi)/(2*8))
    return(np.round(np.dot(np.transpose(passage),np.dot(mat,passage))))
    
def quantification(mat,s) :
    tab=np.copy(mat) 
    for i in range(8) :
        for j in range(8) :
            tab[i][j] = round(mat[i][j]/(1+s*(1+i+j)))

    return(tab) 
    
def dequantification(mat,s) :
    tab=np.copy(mat) 
    for i in range(8) :
        for j in range(8) :
            tab[i][j] = mat[i][j]*(1+s*(1+i+j)) 
    return(tab) 
    
def compression(mat,s) :
    passage=[np.zeros(8) for i in range(8)]
    for i in range(8) :
        for j in range(8) :
            passage[i][j] = c(j)*(np.sqrt(2/8))*np.cos(((2*i+1)*j*np.pi)/(2*8))
    mattcd=np.round(np.dot(np.transpose(passage),np.dot(mat,passage)))
    return(np.round(np.dot(passage,np.dot(dequantification(quantification(mattcd,s),s),np.transpose(passage)))))
    
    
## Sur une image
image=plt.imread('C:\\Users\\qxu\\Documents\\boston.png')
image2=plt.imread('C:\\Users\\qxu\\Documents\\trefle.png')
image3=plt.imread('C:\\Users\\qxu\\Documents\\pd.png')
image4=plt.imread('C:\\Users\\qxu\\Documents\\kalash.png')
"""def decoupage(mat) :
    (n,m,k) = np.shape(mat) 
    n2=n//8
    m2=m//8
    for i in range(n2) :
        for j in range(m2) :
            l.append(mat[i:i+1(8)][j:j+1])"""

def pour_huffman(mat,s) :
    (n,m) = np.shape(mat) 
    mat_comp=np.copy(mat)
    n2=n//8
    m2=m//8 
    for i in range (n2) :
        for j in range(m2) :
            mat88=mat_comp[i*8:(i+1)*8,j*8:(j+1)*8]*255
            mat88_comp=quantification(tcd(mat88),s)
            mat_comp[i*8:(i+1)*8,j*8:(j+1)*8] = mat88_comp/255
    return(mat_comp)
    
def jpeg(mat,s) :
    (n,m) = np.shape(mat) 
    mat_comp=np.copy(mat)
    n2=n//8
    m2=m//8 
    for i in range (n2) :
        for j in range(m2) :
            mat88=mat_comp[i*8:(i+1)*8,j*8:(j+1)*8]*255
            mat88_comp=compression(mat88,s)
            mat_comp[i*8:(i+1)*8,j*8:(j+1)*8] = mat88_comp/255
    return(mat_comp)
             

def composante(mat,a) :
    (n,m,k)=np.shape(mat) 
    mata=[np.zeros(m)for j in range(n)]
    for i in range(n) :
        for j in range(m) :
            mata[i][j]=mat[i][j][a] 
    return(mata)
    
def comp(mat,s) :
    mat_comp=np.copy(mat)
    (n,m,k)=np.shape(mat) 
    for l in range(3) :
        matl=mat[:,:,l]
        mat_comp[:,:,l]=jpeg(matl,s)
    plt.imshow(mat_comp)
    plt.show()
    return()
        
        
##Variante avec fft 

def fft_recursive(A):
    n=len(A)
    if n==1:
        return(A)
    wn=exp(-2*pi*1j/n)
    w=1
    A0=[A[2*k] for k in range(0,n//2)]
    A1=[A[2*k+1] for k in range(0,n//2)]
    Y0=fft_recursive(A0)
    Y1=fft_recursive(A1)
    Y=[0 for i in range(n)]
    for k in range(0,n//2):
        Y[k]=Y0[k]+w*Y1[k]
        Y[k+n//2]=Y0[k]-w*Y1[k]
        w=w*wn
    return(Y)

def G(mat,u,y):
    A=[mat[x][y] for x in range(T)]
    return ( fft_recursive(A) )
    
def F(mat,u,v):
    A=[G(mat,u,y) for y in range(T)]
    return ( fft_recursive(A) )

def FFT2D(mat):
    n=len(mat)
    FFTmat=[[F(mat,u,v) for u in range(n)] for v in range(n)]
    return (FFTmat)
def tcd2 (mat) :
    res = [np.zeros(2*8-1)for i in range(2*8-1)]
    for i in range(2*8-1) :
        for j in range(2*8-1) :
            if i>=7 and j>=7 :
                res[i][j] = mat[i-7][j-7]
            if i<7 and j>=7 :
                res[i][j] = mat[-1-(i-7)][j-7]
            if i>=7 and j<7 :
                res[i][j] = mat[i-7][-1-(j-7)] 
            if i<7 and j<7 :
                res[i][j] = mat[-1-(i-7)][-1-(j-7)] 
    fftmat=FFT2D(res) 
    return(FFT2D(fftmat[7:,7:]))

def tcd2_inverse(mat) :
    res = [np.zeros(2*8-1)for i in range(2*8-1)]
    for i in range(2*8-1) :
        for j in range(2*8-1) :
            if i>=7 and j>=7 :
                res[i][j] = mat[i-7][j-7]
            if i<7 and j>=7 :
                res[i][j] = mat[-1-(i-7)][j-7]
            if i>=7 and j<7 :
                res[i][j] = mat[i-7][-1-(j-7)] 
            if i<7 and j<7 :
                res[i][j] = mat[-1-(i-7)][-1-(j-7)] 
    fftmat=FFT2D(res) 
    return(FFT2D(fftmat[7:,7:]))

    
def compression2(mat,s) :
    mat_cos=tcd2(mat)
    return(tcd2_inverse(dequantification(quantification(mat,s),s)))
    
##huffman 


## Huffman semi-adaptatif

def huffman(tab): # tab contient les [f(a),"a"] où f est la fréquence. On suppose qu'il y a au moins 2 caractères
    tab.sort()
    arbre = [tab[0], [tab[0][0] + tab[1][0]], tab[1]] #(feuille, frequence du noeud, feuille). Les noeuds sont des listes de len 1, les feuilles des listes de len 2
    return huffman_aux(arbre, [[ tab[0][0] + tab[1][0] ]] + tab[2:]) #retourne l'arbre de huffman associé à tab
    
def huffman_aux(arbre,tab):
    if len(tab) < 2:
        return arbre
    else:
        f = tab[0][0]  #frequence du noeud de arbre
        tab.sort()
        if len(tab[0]) == len(tab[1]) == 2:     #ie si le noeud n'est pas dans les 2 premieres cases
            tab2 = [k for k in tab if len(k)==2]    #on retire f de tab pour l'appel récursif
            arbre_2 = [tab[0], [tab[0][0] + tab[1][0]], tab[1]]
            if tab[0][0] + tab[1][0] < f :
                new_arbre = [arbre_2, [f + tab[0][0] + tab[1][0]], arbre]
            else:
                new_arbre = [arbre, [f + tab[0][0] + tab[1][0]] , arbre_2]
            return huffman_aux(new_arbre, [[f + tab[0][0] + tab[1][0]]] + tab2[2:]) 
        elif len(tab[0]) == 1:  # si le noeud est en premiere position
            new_arbre = [arbre, [f + tab[1][0]], tab[1]]
            return (huffman_aux(new_arbre, [[f + tab[1][0]]] + tab[2:]))
        else:   # si le noeud est en 2eme position
            new_arbre = [tab[0], [f + tab[0][0]], arbre]
            return (huffman_aux(new_arbre, [[f + tab[0][0]]] + tab[2:]))
        

def tab_frequences(str): #crée le tableau des frequences pour un texte
    n = len(str)
    caracteres = []
    frequences = []
    for i in str:
        if not i in caracteres:
            caracteres.append(i)
            frequences.append(1/n)
        else:
            for k in range(len(caracteres)):
                if i == caracteres[k]:
                    frequences[k] = frequences[k] + 1/n 
    return [[frequences[i], caracteres[i]] for i in range(len(caracteres))]
    
def in_arbre(arbre, ch):
    if len(arbre) == 2 :  # alors c'est une feuille
        return arbre[1] == ch
    elif len(arbre) ==3 :
        return( in_arbre(arbre[0], ch) or in_arbre(arbre[2], ch) )
    else:
        return False
    
def code_huffman(arbre, ch): #code d'un caractère
    if len(arbre)==2:
        if arbre[1] == ch:
            return("")
    elif in_arbre(arbre[0],ch):
        return "0"+code_huffman(arbre[0], ch)
    elif in_arbre(arbre[2], ch):
        return "1"+code_huffman(arbre[2], ch)
    else:
        return "*"
        
    
def comp_huffman(str):
    tab = tab_frequences(str)
    arbre = huffman(tab)
    str2 = ""
    for ch in str:
        str2 = str2 + code_huffman(arbre,ch)
    return (str2, arbre)

def decomp_huffman_aux(str, arbre, indice): #indice est l'indice du premier bit codant un caractère, la fonction trouve le caractere et l'indice du début du code du suivant
    if len(arbre) == 2:
        return (arbre[1], indice)
    else:
        return ( decomp_huffman_aux(str, arbre[2*int(str[indice])], indice+1) ) #si on lit un 0 on va à gauche, sinon à droite
        
def decomp_huffman(str, arbre):
    texte = ""
    indice = 0
    while indice < len(str):
        x = decomp_huffman_aux(str ,arbre, indice)
        texte = texte + x[0]
        indice = x[1]
    return texte

## Huffman adaptatif
def ascii_to_binaire(ch):
    n = ord(ch)
    res = ""
    c = -1
    while c != 0:
        if n%2 == 1:
            res = "1" + res
        else:
            res = "0" + res
        c = n//2
        n = c
    while len(res)<7:
        res = "0" + res
    return(res)
    
def chaine_binaire_to_ascii(str):
    code = 0
    taille = 0
    for i in str:
        code = 2*code + int(i)
    return chr( code ) # chr donne le caractere codé par le code
    

def new_ch(ch, tab): # ajoute ch à tab et renvoie l'arbre auquel on a ajouté ch
    tab.append([1,ch]) # on compte le nombre de caractères et pas leur fréquence, ce qui revient au même pour l'arbre
    return huffman(tab)
        

def comp_ad_huffman(str):
    arbre = [[0,""]]
    tab = [[0,""]]
    res = ""
    for ch in str:
        if in_arbre(arbre, ch):
            res = res + code_huffman(arbre,ch)
            for i in tab:
                if i[1]==ch:
                    i[0]+=1 # on incrémente ch
            arbre = huffman(tab) # on met à jour l'arbre
        else:
            res = res + code_huffman(arbre,"") + ascii_to_binaire(ch) # on code "" (pour prévenir du code ascii) puis ch en ascii
            arbre = new_ch(ch, tab) # on met à jour l'arbre
    return res


def decomp_ad_huffman(str):
    arbre = [[0,""]]
    tab = [[0,""]]    # on mettra tab et arbre à jour exactement comme on le fait pour la compression
    res = ""
    indice = 0
    while indice < len(str):
        if decomp_huffman_aux(str,arbre,indice)[0] == "":   # si on trouve "", le code suivant sera le code ascii d'une nouvelle lettre
            indice = decomp_huffman_aux(str,arbre,indice)[1] # on saute le code de ""
            ch = chaine_binaire_to_ascii( str[indice:indice+7] ) # puis on prend la lettre codée en ascii sur 7 bits
            res = res + ch
            indice += 7 
            arbre = new_ch(ch, tab) # on met l'arbre et le tableau à jour en ajoutant ch
        else:
            l = decomp_huffman_aux(str,arbre,indice)
            indice = l[1] 
            res = res + l[0] # le caractere est ici codé par l'arbre de huffman
            for i in tab: # on met à jour l'arbre et le tableau dans le cas d'une lettre deja présente
                if i[1]==l[0]:
                    i[0]+=1 
            arbre = huffman(tab)
    return res
            
    
## compression avec huffman 
def mat_to_li(mat) :
    (m,n)=np.shape(mat)
    res=[]
    for i in range(m) :
        for j in range(n) :
            res.append(mat[i][j])
    return(res)
    
def compression_image_huffman(mat,s) :
    (m,n,l)=np.shape(mat)
    res=''
    for k in range(l) :
        (a,b)=comp_ad_huffman(mat_to_li(jpeg(mat[:,:,k],s)))
        res+=a
    return(res)
    
def mat_to_str_zigzag(mat) : #avec zigzag#
    (m,n)=np.shape(mat)
    mat2=np.copy(mat)
    res=''
    haut=1
    bas=0
    x=0
    y=0
    res+=str(mat2[0,0])
    while x!=n-1 or y!=m-1 :
        if x==0 and y!=m-1 and  haut==1 :
            y+=1
            haut=0
            res+= ' ' + str(mat2[x,y])
        elif x==0 and haut==0 :
            y+=-1
            x+=1
            bas=1
            res+= ' ' + str(mat2[x,y])
        elif y==0 and x!=n-1 and             bas==1 :
            x+=1
            bas=0
            res+= ' ' + str(mat2[x,y])
        elif y==0 and bas==0 :
            y+=1
            x+=-1
            haut=1
            res+= ' ' + str(mat2[x,y])
        elif x==n-1 and bas==1 :
            y+=1 
            bas=0
            res+= ' ' + str(mat2[x,y])

        elif x==n-1 and  bas==0 :
            y+=1
            x+=-1
            haut=1
            res+= ' ' + str(mat2[x,y])
        elif y==m-1 and   haut==1 :
            x+=1
            haut=0
            res+= ' ' + str(mat2[x,y])
        elif y==m-1 and haut==0 :
            y+=-1
            x+=1
            bas=1
            res+= ' ' + str(mat2[x,y])
        elif bas==1 :
            y+=-1
            x+=1
            bas=1
            res+= ' '+  str(mat2[x,y])
        elif haut==1 :
            y+=1
            x+=-1
            haut=1
            res+= ' ' + str(mat2[x,y])
        
        
    return(res) 





def compression_image_ad_huffman(mat,s) :
    (m,n,l)=np.shape(mat)
    res=''
    for k in range(l) :
        a=comp_ad_huffman(mat_to_str_zigzag(pour_huffman(mat[:,:,k],s)))
        res+=a
    return(res)
        