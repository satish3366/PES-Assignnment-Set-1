print("printing values from 1 to 100 using for loop:")
print([i for i in range(101)])
print("printing values from 100 to 1  using while loop:")
i=100
while(i>=1):
    print(i,sep=' ')
    i=i-1
print("taking a string as hello world printing string letter by letter")
st="Hello World!"
for i in st:
    print(i,sep="\n")
