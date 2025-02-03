n=int(input("Enter the digit:"))
temp=n
sum=0
for i in range(0,n+1):
    d=n%10
    sum=sum+d
    n=n//10
print(sum)