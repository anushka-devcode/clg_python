x=int(input("Enter the value:"))
y=int(input("Enter the value:"))

op=input("choose option\n1.Addition\n2.Substraction\n3.multiplication\n4.Division\n5.Modulus\n")
print("your choice:")
sum=x+y
sub=x-y
mal=x*y
div=x/y
mod=x%y

if(op=="1"):
    print("Sum is:",sum)
elif(op=="2"):
    print("Subs is:",sub)
elif(op=="3"):
    print("multiply is:",mal)
elif(op=="4"):
    print("divide is:",div)
elif(op=="5"):
    print("modulud is:",mod)
else:
    print("invalid choice")
