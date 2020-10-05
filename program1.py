x1 = [3, 10, 5, 25, 2, 8]
c=0
for i in range(0,len(x1)-1):
    for j in range(0,len(x1)-1):
            if i!=j:
                c1=(x1[i]^x1[j])
                if (c<c1):
                    c=c1
print(c)                
