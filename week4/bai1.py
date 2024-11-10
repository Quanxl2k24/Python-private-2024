k = int(input())
a=[]
for i in range(k):
   a.append(int(input())) 

n = int(input())
m = int(input())
tmp = 0

if m*n < k:
   for i in range (n):
      tmp +=m
      print(a[tmp-m:tmp])
else :
   print("KHONG the tao dc mang hai chieu nhu yeu cau!")