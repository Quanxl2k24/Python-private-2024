string = input("Nhap chuoi ki tu: ")
a = {}

for i in string:
    if i.isalpha():
        i= i.lower()
        if i in a:
            a[i]+=1
        else:
            a[i]=1
print(a)