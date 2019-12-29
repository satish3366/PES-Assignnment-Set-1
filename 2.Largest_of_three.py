A=int(input("enter number A:"))
B=int(input("enter number B:"))
C=int(input("enter number C:"))
if(A >= B and A >= C):
    print("A is the largest number:", A);
elif(B >= A and B >= C):
    print("B is the largest number:", B);
else:
    print("C is the largest number:", C);
