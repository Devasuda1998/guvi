q=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(q):
    l.sort(reverse=True)
print(*l,sep="\n")
