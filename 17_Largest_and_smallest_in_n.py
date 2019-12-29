l=[]
l=list(map(int,input('enter values to find largest and smallest:').split()))
print("list values:",l)
print("largest value is :",sorted(l)[-1])
print("smallest value is :",sorted(l)[0])
