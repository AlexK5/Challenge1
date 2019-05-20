import math
def isprime(n):
  y=2
  while y<=math.sqrt(n):
    if n%y==0:
      return(0)
    y+=1
  return(1)
x=2
total=0
while x<3000:
  if isprime(x)==1:
    total+=x
  x+=1
print(total)
