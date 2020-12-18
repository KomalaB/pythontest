####2. Accept 2 nuwmbers and display the smallest of the two
def small(num1,num2):
    while (num1!=num2):
           if num1 < num2:
               print(+num1, " is the smallest number")
               return num1
            #  break
           else:
                print(+num2, " is the smallest number")
                return num2
           break
    if num1 == num2:
            print("Both Numbers are equal")
            num2=int(input("if you wish to compare again, please re-enter unique 2nd number : "))
            small(num1,num2)
    #else:
     #       small(num1, num2)
            # break
 
num1=int(input("enter the first number : "))
num2=int(input("enter the 2nd number : "))
#print(num2)

##
##if num1==num2:
##    print("Both Numbers are equal")
##    num2=int(input("if you wish to compare again, please re-enter unique 2nd number : "))
##    small(num1, num2)
##elif num1>num2 or num2>num1:
##    small(num1, num2)
#else:
 #   mini=small(num1, num2)
small(num1, num2)
#print(+mini, " is the smallest number")
#mini=small(num1,num2)


##mini=small(num1,num2)
##print(+mini, " is the smallest number")
#-----------------------------

#Method 2 :
##num1=int(input("enter the first number : "))
##num2=int(input("enter the 2nd number : "))
##
##if num1==num2:
##        print("Both Numbers are equal")
##else:
##        minimum = min(num1, num2)
##        print(+minimum, "is the Smallest number")
##
##

