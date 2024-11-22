x = int(input("Nhap x: "))
n = 1000
tg = 0;

def giaithua(n):
    tmp = 1;
    for i in range(1,n+1):
        tmp *= i
    return tmp;

for i in range (n):
    tg += (x**i) / (giaithua(i))

print(tg)