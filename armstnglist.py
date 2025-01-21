u_list=input("Enter the yr:").split()
u_list=[int (i) for i in u_list]
sum =0
size=len(u_list)
for i in u_list:
    sum=sum+i**size
sum_list=[]
temp=sum
while(temp!=0):
    sum_list.append(temp%10)
    temp=temp//10
sum_list=sum_list[::-1]
if(sum_list==u_list):
    print("Armstrong")
else:
    print("not Armstrong")