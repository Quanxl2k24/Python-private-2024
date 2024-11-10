
a=[]
b=[]

n = int(input())
m = int(input())

for i in range(n):
    a.append(input())

for i in range (m):
    b.append(input())

def cauclate(a,b):
    c=[]
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        if i < len(a):
            c.append(a[i])
            i +=1
        if j < len(b):
            c.append(b[j])
            j +=1
    print(c)
cauclate(a,b)