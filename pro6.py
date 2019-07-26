q=int(input())
r=input()
c=[]
count=0
b=(r.split(" "))
for n in b:
    c.append(int(n))
for i in range(0,len(c)):
    for j in range(i+1,len(c)):
        for k in range(j + 1, len(c)):
            if c[i] < c[j] <c[k]:
                count+=1
print(count)
