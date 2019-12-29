def prime(num):
    if num > 1:
        for i in range(2, num//2):
             if (num % i) == 0:
               print(num, "is not a prime number")
               break
        else:
                print(num, "is a prime number")
    else:
       print(num, "is not a prime number")

n=int(input('enter number to find prime or not: '))
prime(n)
n=int(input('enter number to find prime till N: '))
for num in range(n):
    if num > 1:
        for i in range(2, num//2):
             if (num % i) == 0:
                 break
        else:
                print(num)
