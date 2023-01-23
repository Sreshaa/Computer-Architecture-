n= int(input("enter a decimal:"))
sum=0
m=1
while n>0 :
    r= n%8
    n=n//8
    sum=sum+(r*m)
    m=m*10
print("binary:",sum)
