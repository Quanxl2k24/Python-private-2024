a = int(input("Nhap a:"))

while a!=0:
    tmp = a // 8;
    print(a - 8 * tmp, end = '')
    a = tmp
    
print (dir(a))