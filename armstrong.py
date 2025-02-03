arm=int(input("Enter the value:"))
temp=arm
sum=0
arm_str=str(arm)
size=len(arm_str)

while(arm!=0):
    d=arm%10
    sum=sum+d**size
    arm=arm//10
if(temp==sum):
    print("This is armstrong no.")
else:
    print("not an armstrong no.")