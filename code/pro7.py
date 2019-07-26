import math as m
d=int(input())
for i in range(0,d):
    j=pow(2,i)
    ifj>d:
        j=pow(2,i,-1)
        break
c=d-j
print(c)
