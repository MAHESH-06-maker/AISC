import numpy as np 
import matplotlib.pyplot as plt 
x = np.arange(0,101,1)
def triangular(x ,a , b, c):
    V = []
    for v in x: 
        if v<a or v>c:
            V.append(0)
        elif v == b:
            V.append(1)
        elif v < b:
            V.append((v-a)/(b-a))
        else:
            V.append((c-v)/(c-b))
    return V
def trapezoildal(x ,a , b, c , d):
    y = []
    for v in x: 
        if v<a or v>d:
            y.append(0)
        elif b<=v<=c:
            y.append(1)
        elif  a<= v < b:
            y.append((v-a)/(b-a))
        else:
            y.append((d-v)/(d-c))
    return y
def Gaussian(x, mean , sigma):
    return np.exp((-(x-mean)**2)/(2*sigma**2))
plt.figure(figsize=(9,10))
plt.subplot(3,1,1)
plt.plot(x,triangular(x,0,20,50) , label="weak")
plt.plot(x,triangular(x,20,50,80) , label="medium ")
plt.plot(x,triangular(x,60,70,100) , label="strong")
plt.title("Traingular")
plt.xlabel("soil level")
plt.ylabel("membership")
plt.legend()
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(x, trapezoildal(x,0,0,20,50,) , label="weak")
plt.plot(x, trapezoildal(x,10,20,50,80) , label="medium ")
plt.plot(x, trapezoildal(x,60,70,80,100) , label="strong")
plt.title("Trapezoidal")
plt.xlabel("soil level")
plt.ylabel("membership")
plt.legend()
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(x,Gaussian(x,15,15) , label="weak")
plt.plot(x,Gaussian(x,20,15) , label="medium ")
plt.plot(x,Gaussian(x,50,15) , label="strong")
plt.title("Gaussian")
plt.xlabel("soil level")
plt.ylabel("membership")
plt.legend()
plt.grid(True)
plt.show()
plt.tight_layout(True)


