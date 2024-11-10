n = int(input())
m = int(input())
a=[]
b=[]
c=[]
for i in range(n):
    a.append(int(input()))

for i in range(m):
    b.append(int(input()))

for i in range (n):
    for j in range(m):
        if a[i] == b[j]:
            c.append(a[i])
            break
print(c)
