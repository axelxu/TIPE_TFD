i=complex(0,1)
import numpy as np


def fft_recursive(A):
    n=int(len(A))
    if n==1:
        return(A)
    wn=np.exp(2*i*np.pi/n)
    w=1
    A0=np.array([A[2*k+1] for k in range(0,int(n/2))])
    A1=np.array([A[2*k] for k in range(0,int(n/2)-1)])
    Y0=fft_recursive(A0)
    Y1=fft_recursive(A1)
    Y=np.zeros(n)
    for k in range(int(n/2)):
        Y[k]=Y0[k]+w*Y1[k]
        Y[k+n/2]=Y0[k]-w*Y1[k]
        w=w*wn
    return(Y)
        
        
