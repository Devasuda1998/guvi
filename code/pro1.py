p=[]
b=int(input())
for k in range(0,b):
    n=input()
    p.append(n)
st=""
count=0
t=[]

for l in p:
    t.append(len(l))
t.sort()
m=t[0]
z=0

for j in range(0,m):
    count=0
    for i in range(1,b):

        if p[i-1][j]==p[i][j]:
            count+=1
        else:
            z=1
            break
        if count==b-1:
            st=st+(p[i][j])
    if z==1:
        break
print(st)
