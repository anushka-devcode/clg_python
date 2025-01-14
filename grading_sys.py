n=int(input("Enter the marks"))
if(n>90):
    print("GRADE:A+")
elif(n>80 and n<=90):
    print("GRADE:A")
elif(n>70 and n<=80):
    print("GRADE:B+")
elif(n>60 and n<=70):
    print("GRADE:B")
elif(n>50 and n<=60):
    print("GRADE:C+")
elif(n>40 and n<=50):
    print("GRADE:C")
elif(n>35 and n<=40):
    print("GRADE:D")
else:
    print("FAIL need to progress")