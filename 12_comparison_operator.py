l=list(map(int,input("enter values:").split()))
#print(type(l[0]))
print(l)
a=sum(l)/len(l)
c=0
for i in range(len(l)):
    if(l[i]<=a):
        c+=1
        print(l[i])
print("count of small elements:",c)
for i in range(len(l)):
    if(l[i]>=a):
        c+=1
        print(l[i])
print("count of large elements:",c)
c=0
for i in range(len(l)):
    if(l[i]==a):
        c+=1
        print(l[i])
print("count of equal elements:",c)
