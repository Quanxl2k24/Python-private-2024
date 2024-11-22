a = "2[abc]3[cd]ef"
b=''
tmp = 0
i = 0
while i < len(a):
    if a[i].isdigit()==1:
        tg = int(a[i])
        tg_1=0

        for j in range(i,len(a)):
            if a[j] == "]":
                tg_1=j
                break

        b += a[i+2:j]*tg
        i = j + 1
        
    else:
        b+=a[i]
        i+=1
print(b)
