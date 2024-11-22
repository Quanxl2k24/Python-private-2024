a = "2[abc]3[cd]ef"
tmp = 0
for i in range(len(a)):
    if a[i].isdigit()==1:
        tg_1=0
        for j in range(i,len(a)):
            if a[j] == "]":
                tg_1=j
                break
        b = a[i+1:j]*3
print(b)
