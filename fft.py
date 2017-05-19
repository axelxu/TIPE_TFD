from cmath import exp
from cmath import pi
import numpy as np

A=[0.5,1,1,1,0.5,0,0,0]
z1=complex(0,1+2**(1/2))
z2=complex(0,1-2**(1/2))
FA=[4,-z1,0,z2,0,-z2,0,z1]

z3=complex(2,-2)
z4=complex(2,2)
C=[4,3,2,1]
FC=[10,z3,2,z4]

 
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
    
def fft_inverse(B):
    n=len(B)
    if n==1:
        return(B)
    wn=exp(2*pi*1j/n)
    w=1
    B0=[B[2*k] for k in range(0,n//2)]
    B1=[B[2*k+1] for k in range(0,n//2)]
    Y0=fft_inverse(B0)
    Y1=fft_inverse(B1)
    Y=[0 for i in range(n)]
    for k in range(0,n//2):
        Y[k]=Y0[k]+w*Y1[k]
        Y[k+n//2]=Y0[k]-w*Y1[k]
        w=w*wn    
    return(Y)

def ffti(B):
    n=len(B)
    return([fft_inverse(B)[i]/n for i in range(len(B))]) 
