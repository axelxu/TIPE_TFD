from cmath import exp
from cmath import pi
import numpy as np

m=[[140,144,147,140,140,155,179,175],[144,152,140,147,140,148,167,179],[152,155,136,167,163,162,152,172],[168,145,156,160,152,155,136,160],[162,148,156,148,140,136,147,162],[147,167,140,155,155,140,136,162],[136,156,123,167,162,144,140,147],[148,155,136,155,152,147,147,136]]

def fft(A):
    n=len(A)
    if n==1:
        return(A)
    wn=exp(-2*pi*1j/n)
    w=1
    A0=[A[2*k] for k in range(0,n//2)]
    A1=[A[2*k+1] for k in range(0,n//2)]
    Y0=fft(A0)
    Y1=fft(A1)
    Y=[0 for i in range(n)]
    for k in range(0,n//2):
        Y[k]=Y0[k]+w*Y1[k]
        Y[k+n//2]=Y0[k]-w*Y1[k]
        w=w*wn
    return(Y)

def ffti(B):
    n=len(B)
    conjB=[np.conj(i) for i in B]
    C=fft(conjB)
    conjC=[np.conj(i)/2 for i in C]
    return(conjC)
    
def sym(x):
    n=len(x)
    y=[0 for i in range(2*n)]
    for i in range(0,n):
        y[i]=x[i]
    for i in range(n,2*n):
        y[i]=x[2*n-i-1]
    return(y)
    
def coef(k):
    if k==0:
        return 1/(2**(1/2))
    return 1
    
def DCT(x):
    n=len(x) 
    y=sym(x)
    fy=fft(y)
    dfy=[(coef(k)*exp(-pi*1j*k/(2*n))*fy[k]/n).real for k in range(len(fy)//2)]
    return ( dfy )
            
def G(mat,u,y):
    n=len(mat)
    A=[mat[x][y] for x in range(n)]
    return ( DCT(A)[u] )
    
def F(mat,u,v):
    n=len(mat)
    A=[G(mat,u,y) for y in range(n)]
    return ( DCT(A)[v] )

def DCT2D(mat):
    n=len(mat)
    FFTmat=[[F(mat,u,v)*n/2 for v in range(n)] for u in range(n)]
    return( FFTmat )   
    
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
 
def pour_huffman2(mat,s) :
    (n,m) = np.shape(mat) 
    mat_comp=np.copy(mat)
    n2=n//8
    m2=m//8 
    for i in range (n2) :
        for j in range(m2) :
            mat88=mat_comp[i*8:(i+1)*8,j*8:(j+1)*8]*255
            mat88_comp=quantification(DCT2D(mat88),s)
            mat_comp[i*8:(i+1)*8,j*8:(j+1)*8] = mat88_comp/255
    return(mat_comp) 
    
def compression_image_ad_huffman2(mat,s) :
    (m,n,l)=np.shape(mat)
    res=''
    for k in range(l) :
        a=comp_ad_huffman(mat_to_str_zigzag(pour_huffman2(mat[:,:,k],s)))
        res+=a
    return(res)
    

    