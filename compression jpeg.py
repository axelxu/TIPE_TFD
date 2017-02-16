import numpy as np
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
    
    
    

        
            
    