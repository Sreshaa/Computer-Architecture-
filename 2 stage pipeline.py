a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=4
f=0
ch=int(input("1.ADD,2.SUB,3.MUL,4.DIV:"))
if ch==1:
    res=a+b
elif ch==2:
    res=a-b
elif ch==3:
    res=a*b
elif ch==4:
    if b==0:
        print("Denominator can not be zero:")
        print("wrong input")
        f=1
    else:
        res=a/b
else:
    print("wrong input")

f=1
if f==0:
    print("the cycle value is",f)
ins=int(input("enter no of instructions:"))
print("the performance measure:",ins/c)
print("res =",res)
