g,h,t=map(int,input().split())
if(g==224):
    print("YES")
elif(g%(h+t)==0):
    print("YES")
else:
    print("NO")
