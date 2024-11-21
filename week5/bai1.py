n = int(input("Nhap n: "))
m = int(input("Nhap m: "))

a = [int(input()) for i in range(n)]
b = [input() for i in range(m)]
a = tuple(a)
b = tuple(b)

tmp = 0  
for x in a:
    tmp += x
print(tmp)

tmp = tmp / n  
tg = 0
for x in a: 
    if tmp < x:
        tg += 1
print(f'So phan tu lon hon trung binh cong = {tg}')

a_chan = []
a_le = []

for x in a:
    if x%2 == 0:
        a_chan.append(x)
    else:
        a_le.append(x)
a_chan = tuple(a_chan)
a_le = tuple(a_le)
print(f"tuple chan = {a_chan}")
print(f"tuple le = {a_le}")

def dem_xaukitu (b):
    k = input("nhap ki tu k: ")
    print(f"so lan k xuat hien = {b.count(k)}")
dem_xaukitu(b)

def dem_kitu(b):
    tmp = 0
    for y in b:
        if len(y) >= 5:
            tmp +=1
    print(tmp)
dem_kitu(b)

def kethop_ab(a,b):
    a = list(a)
    b = list(b)
    c = []
    i = 0
    j = 0
    while i < n or j < m:
        if(i < n):
            c.append(a[i])
            i += 1

        if j < m:
            c.append(b[j])
            j += 1
    print(c)
kethop_ab(a,b)