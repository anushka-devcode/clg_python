n="Salve io sono con mia amica"
print(n)
count=0
sb=input("Enter the substring:")
for i in n:
    if(sb==i):
        count+=1
print(count)