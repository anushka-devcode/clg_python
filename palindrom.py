u_list=input("Enter yr no.")
u_list=u_list.split()
print(u_list)
if u_list==u_list[::-1]:
    print("This is palindrome")
else:   
    print("THisis not the palindrome")