n = int(input("Nhap n:"))
k = int(input("Nhap k: "))

a=[]
for i in range(n):
    a.append(int(input()))

def tim_kiem(n,a,k):
    l = 0
    r = n
    while l <= r:
        tmp = (l + r)//2
        if k == a[tmp]:
            return tmp
        if k > a[tmp]:
            l = tmp + 1
        else:
            r = tmp -1
    return -1
c = tim_kiem(n,a,k)

print(c)