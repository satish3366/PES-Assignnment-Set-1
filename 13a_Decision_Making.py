A=int(input("enter number A:"))
B=int(input("enter number B:"))
C=int(input("enter number C:"))
D=int(input("enter number D:"))
if(A >= B and A >= C and A>=D):
    print("A is the largest number:", A);
elif(B >= A and B >= C and  B>=D):
    print("B is the largest number:", B);
elif(C >= A and C >= B and C>=D):
    print("C is the largest number:", C);
else:
    print("D is the largest number:", D)
