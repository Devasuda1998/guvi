ght=int(input())
sums=0
for i in range(0,ght):
    if(pow(2,i)<ght):
        break
    sums=ght-pow(2,i)
print(sums)
