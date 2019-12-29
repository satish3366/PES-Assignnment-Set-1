name=['satish','kumar','puli','john','sai','rajesh','psk','johnny','jagan','mahesh']
id=[11,22,33,44,55,66,77,88,99,100]
print("printing all names on list",name)
n=int(input('enter an index to print the value in index:'))
print(f'name={name[n]} id={id[n]}')
print("printing names from 4th to 9th position",name[4:9])
print("printing names from 3rd position to end of list",name[3:])
n=int(input('enter a number to print the names in n times: n='))
print(name*n)
print(f'concatination of two strings',name+id)
for i in range(len(name)):
    print(name[i].ljust(15,' '),id[i])
