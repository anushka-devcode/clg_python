n=input("Enter the string:")
count=0
for char in n:
    if char.isupper():
        count=count+1
print("Number of uppercase elements are:",count)
