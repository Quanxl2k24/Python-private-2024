import random
n = int(input("Nhap n: "))

a = {}
for i in range(n):
    a[f"account{i+1}"] = {
        'user' : 2023600000+i,
        'password':random.choice(['KTPM','CNTT','KHMT','HTTTT','DAPT']),
    }    
print(a)