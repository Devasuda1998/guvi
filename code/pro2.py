r=(input())
s=r.split("")
c=s[0]
l=len(c)
d=int(s[1])
st=""
count=0
if d!=0:
   for i in range(1,10):
   if str(i) in c:
      f=c.find(str(i))
      c=c[f:]
      st=st+str(i)
      count+=1
   else:
      pass
   if count==l-d:
      print(st)
      break
   if count!=l-d:
      z=l-d-count
      st=st+c[-z:]
      print(st)
   else:
      print(c)
