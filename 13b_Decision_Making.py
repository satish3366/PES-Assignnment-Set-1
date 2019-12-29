A=int(input("enter number A:"))
B=int(input("enter number B:"))
C=int(input("enter number C:"))
D=int(input("enter number D:"))
E=int(input("enter number E:"))
if(A >= B and A >= C and A>=D and A>=E):
    print("A is the largest number:", A);
elif(B >= A and B >= C and  B>=D and B>=E):
    print("B is the largest number:", B);
elif(C >= A and C >= B and C>=D and c>=E):
    print("C is the largest number:", C);
elif(D>=A and D>=B and D>C and D>=E):
    print("D is the largest number:", D)
else:
    print("E is the largest number:", E)
