#Create a dictionary called mydata which holds ID number as key and name of the person as value.   Display the da

Id_num[]
Stu_Name[]
count=int(input("enter the number of IDs you will like to register :")
ct=count

while count >0:
    for i in range(0,count):
        num=input("Enter the unique ID : ")
        name=input("Enter Student Name : ")
        Id_num.append(num)
        Stu_Name.append(name)
    count=count-1

while ct >0:
    print(Id_num : Stu_Name)

print("end of list, thank you") 
