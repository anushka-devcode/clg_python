grd=(input("Enter the marks")).split()
print(grd)
gr=[]
grd=[int (i) for i in grd]
grd.sort(reverse=True)
for i in grd:
    if(grd(i)>90):
        gr='A+'
        grd.append(gr)
        print("GRADE:A+")
    elif(grd(i)>80 and grd(i)<=90):
        gr='A'
        grd.append(gr)
        print("GRADE:A")
    elif(grd(i)>70 and grd(i)<=80):
        gr='B+'
        grd.append(gr)
        print("GRADE:B+")
    elif(grd(i)>60 and grd(i)<=70):
        gr='B'
        grd.append(gr)
        print("GRADE:B")
    elif(grd(i)>50 and grd(i)<=60):
        gr='C+'
        grd.append(gr)
        print("GRADE:C+")
    elif(grd(i)>40 and grd(i)<=50):
        gr='C'
        grd.append(gr)
        print("GRADE:C")
    elif(grd(i)>35 and grd(i)<=40):
        gr='D'
        grd.append(gr)
        print("GRADE:D")
    else:
        gr='Fail'
        grd.append(gr)
        print("FAIL need to progress")
print(gr)