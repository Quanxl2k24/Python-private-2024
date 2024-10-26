print("Chao mung den CLB Tin Hoc HIT")

print("CLB Tin Hoc HIT truc thuoc Khoa CNTT  - “10 diem”")

a = "CLB Tin Hoc HIT truc thuoc khoa CNTT"

print("in ra cac chu cai in hoa")
for A in a:
    tmp1 = A.isupper()
    if(tmp1 == True):
        print(A, end = '')

print(" ")

print("in ra cac chu cai thuong")
for B in a:
    tmp2 = B.islower()
    if(tmp2 == True):
        print(B, end = '')

print(" ")


if "CNTT" in a:
    print("YES")
else:
    print("NO")

for C in a:
    tmp3 = C.isupper()
    if(tmp3 == True):
        print(C.lower(),end = '')
    else:
        print(C.upper(), end = '')