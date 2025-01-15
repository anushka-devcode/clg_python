n=int(input("enter the no:"))
if(n>1):
    for i in range(2,(n**0.5)+1):
        if(n%i==0):
            print(n,"is not a prime no>>")
        else:
            print(n,"is a prime no.")
else:
    print(n,"is not a prime no>>")
    
    