a = 5
b = 3
c = 3.3
d = "hello"

#print(a, b, c)
#print("type(a)=", type(a)) #xem kieu du lieu
#print("type(d)=", type(d)) #xem kieu du lieu

#Cac phep toan tu so hoc
print("a - b = ", a - b)
#print("a*d=", a*d)
print("a + b = ", a + b)
print ("a // b = ", a//b)
print("a ** b = ", a**b )

#Cac toan tu so sanh
#Toan tu logic
if a > 0 and b > 0:
    print ("dieu kien thoa man")

if (a > 0 or b > 0):
    print("dieu kien thoa man")

#toan tu gan 
string = "Study python with HIT"
print("string =", string)
print(f"len(string)={len(string)}")
print(f"string[-6]={string[-6]}")
print(f"string[-6]={string[-len(string)]}")
print(f"string[0:3]={string[0:3]}")
print(string.lower())
print(string.upper())

print(string.replace('y', "  Hello  "))









