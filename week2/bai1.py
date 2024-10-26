a = 50
b = 20

print("a + b = ",a + b)
print("a - b = ",a-b)
print("a * b = ",a*b)
print("a / b = ",a//b)
print("a**b = ",a**b)
print("a % b = ",a%b)

if a>b:
    print("a>b")
else:
    print("a<=0")

if a > 0 and b > 0:
    print("a và b lớn hơn không")

print(a or b)

c = a ^ b

print("ket qua cua a ^ b la:",c)

d = not a 
print("not a = ", d)

e = a >> 5
print("a dich phai 5 bit:",e)

f = a << 5 
print ("a dich trai 5 bit la:",f)

binary_str = bin(a)[2:] 

reversed_binary_str = binary_str[::-1]  

reversed_decimal = int(reversed_binary_str, 2)

print("Giá trị thập phân của chuỗi nhị phân đảo ngược:", reversed_decimal)
