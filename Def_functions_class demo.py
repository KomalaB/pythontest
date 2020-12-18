
def rock():
    a=input("age: ")
    n=input("name: ")
    print(n + " " +a)
rock()
#####
def func(name,age):
    print("My name is " + name + " and I am "+ age+ " years old")
func("fatih", "37")
#####
def greetall():
    return "Hello all!"
message=greetall()
print(message)
#####
myList=[]
def greetlist():
    myList=["Hi", "Hello", 100, 25, "Bye"]
    return myList
print(greetlist())
#####
def printgenius(name):
    return name + " is a genius"
print(printgenius("Lee"))
studentName=input("Enter student name: ")
data=printgenius(studentName)
print(data)
#####
