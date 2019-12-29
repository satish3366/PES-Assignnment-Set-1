name=['satish','kumar','puli','john','sai']
c=input("enter element to check in list:")
print("********************using IN list menthod*********************")
if c in name:
    print("element found")
else:
    print("element not found")
print("******************without using IN meathod********************")
n=0
for i in range(len(name)):
    if(c==name[i]):
        print("element found")
        n=1;
if n==0:
    print("element not found")
print("printing elements in reverse      ",name[::-1])
