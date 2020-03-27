import math
import matplotlib.pyplot as plt

x =[ i/100 for i in range(-350,351,1) ]

R = 6.33
C = 1/R
K = 0
e = math.exp(1)
A = [0, 0, 0, 0, 6.89*(e**-4) ,0, -6.09*(e**-5), 0, 9.2*(e**-6), 0, -2.28*(e**-8)]

Z=[]
for i in x:
    T = (1+K)*(C**2)*(i**2)
    T2 = 1 + (1-T)**2
    T3 = (C*(i**2)) / T2 
    T4 = A[4]*(i**4)
    T6 = A[6]*(i**6)
    T8 = A[8]*(i**8)
    T10 = A[10]*(i**10)
    T_final = T3 + T4 + T6 + T8 + T10
    Z.append(T_final)

plt.plot(x,Z)

Z_shrink = [ 1.005 * i for i in Z ]
plt.plot(x,Z_shrink)

Z_diff = [0.005 * i for i in Z]
plt.plot(x,Z_diff)

plt.show()
