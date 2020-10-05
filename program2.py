z=[2,1,4,3,7]
x=9
for i in range(0,len(z)):
    for j in range(0,len(z)):
        if z[i]+z[j]==x:
            print(i,j)
