print "The numbers from 1 to 100 skipping odd numbers using while loop is below:"
i=1
while i<=100:
  if i%2!=0:
    i+=1
    continue
  print i
  i+=1
print "\n\n"

print "Breaking the for loop i ==50"
i=1
while i<=100:
  if i==50:
    break
  print i
  i=i+1
print "using continue for the values 10,20,30,40,50"
i=1
while i<=100:
  if i==10 or i==20 or i==30 or i==40 or i==50:
    i=i+1
    continue
  print i
  i=i+1
print "\n"
