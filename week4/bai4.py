import random
import math

n = int(input("Nhap n "))
a=[]
b=[]



for i in range(n):
    a.append(random.uniform(1.0, 10.0))
    b.append(random.uniform(1.0, 10.0))
print(a)
print(b)

def MAS(a,b,n):
    tmp = 0
    for i in range(n):
        tmp += abs(a[i] - b[i])
    return (1/n)*tmp

def MSE(a,b,n):
    tmp = 0
    for i in range(n):
        tmp +=(a[i] - b[i])**2
    return (1/n)*tmp

def RMSE(a,b,n):
    return MSE(a,b,n)**(1/2)

def Huber_loss(a,b,n):
    tg= 0.5
    tmp = 0
    for i in range(n):
        if abs(a[i] - b[i]) < tg:
            tmp += tg*((a[i] - b[i])**2)
        else:
            tmp += tg*(abs(a[i] - b[i]) - 1/2*tg)
    return tmp*(1/n)

m = input("Nhap ten loss game: ")
# m = m.upper()
# print(m)

if m == 'MAS':
    print(MAS(a,b,n))
elif m == 'MSE':
    print(MSE(a,b,n))
elif m == 'RMSE':
    print(RMSE(a,b,n))
elif m == 'Huber_loss':
    print(Huber_loss(a,b,n))