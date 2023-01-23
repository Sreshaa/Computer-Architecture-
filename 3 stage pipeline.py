a= int(input("enter n0.1:"))
b= int(input("enter no.2:"))
c=4
AND=a&b
OR=a|b
NAND=~AND
print("the cycle value is:",c)
ins=int(input("enter no. of instructions:"))
print("the performance measure:",ins/c)
print("result AND:",AND)
print("result OR:",OR)
print("result NAND:",NAND)
