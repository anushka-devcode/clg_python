
'''student_data = {"Anushka": {"Math": "Abhishek Sir", "DSA": "Vishal Sir","Python":"Ravi Sir"},"Vanshika": {"Math": "Abhishek Sir", "COA": "Sushabhan Sir","DE":"Rakesh Sir"},"Ritkriti": {"Maths": "Saurabh Sir", "History": "Suresh Sir"}}'''
stu_data={}
n1=int(input("Enter the no of student:"))
for i in range(n1):
    stu_name=input("Enter the name of students:")
    stu_data[stu_name]={}
    num_sub=int(input("Enter the no of subjects:"))
    for i in range(num_sub):
        stu_sub=input("Enter subject name: ")
        tch=input("Entert teacher name:")
        stu_data[stu_name][stu_sub]=tch

stu=input("Enter the name u want to search:")
sub=input("Enter the subject:")
if stu in stu_data:
    if sub in stu_data[stu]:
        teacher_name = stu_data[stu][sub]
        print(f"Teacher for {stu} in {sub}: {tch}")
    else:
        print(f"{stu} is not enrolled in {sub}.")
else:
    print("Student not found.")
