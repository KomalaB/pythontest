####1. write a program which takes 3 numbers from user. and prints the total amd product of the numbers.
##from Vijaya to everyone:    12:09 PM
##2. Repeat the above process 3 times

def zero(num1,num2,num3):
   if num1==0:
        print("1st input is zero")
        reply = input("Do you wish to enter non-zero number : y/n ? ---> "  )
        if reply=="y":
            num11=int(input("please re-enter another non-zero number: "))
            mul(num11,num2,num3)
            add(num11,num2,num3)
                #break
          #  return mul11+num2+num3
        
   if num2==0:
        print("2nd input is zero")
        reply = input("Do you wish to enter non-zero number : y/n ? ---> "  )
        if reply =="y":
            num11 = int(input("please re-enter another non-zero number: "))
            mul(num1,num11,num3)
            add(num1,num11,num3)
            
        #break
         #   return num1+num2+num3
     
   if num3==0:
        print("3rd input is zero")
        reply = input("Do you wish to enter non-zero number : y/n ? ---> "  )
        if reply=="y":
            num11 = int(input("please re-enter another non-zero number: "))
            mul(num1,num2,num11)
            add(num1,num2,num11)
            
        #break
           # return num11#+num2+mul2

def mul(num1,num2,num3):
    if num1>0 and num2>0 and num3>0:
        mul1=num1*num2*num3
        print("\n", +mul1, "is the product of given numbers")
        print("multiplication task Completed, thank you")
               # return(mult1)
    elif num1==0 or num2==0 or num3==0:
        zero(num1,num2,num3)
        
       # mul(num1,num2,num3)
    #else:
     #   print("multiplication task Completed, thank you")

        
def add(num1,num2,num3):
    if num1>0 and num2>0 and num3>0:
        addi=num1+num2+num3
        print("\n", +addi, "is the sum of given numbers")
        print("Addition task Completed, thank you")
        #return(addi)
##    elif num1==0 or num2==0 or num3==0:
##        addi = num11+num1+num2+num3
##        print("\n", +addi, "is the sum of given numbers")
##        print("Addition task Completed, thank you")
##

    
       # mul(num1,num2,num3)
#        print("Task Completed, thank you")
   # return addi
##    elif num1==0 or num2==0 or num3==0:
##     mult2=   zero(num1,num2,num3)
##        mul(
##    
##
##        
##           if num1 < num2:
##               print(+num1, " is the smallest number")
##               return num1
##            #  break
##           else:
##                print(+num2, " is the smallest number")
##                return num2
##           break
##    if num1 == num2:
##            print("Both Numbers are equal")
##            num2=i5nt(input("if you wish to compare again, please re-enter unique 2nd number : "))
##            small(num1,num2)
    #else:
     #       small(num1, num2)
            # break5
 
num1=int(input("enter the first number : "))
num2=int(input("enter the 2nd number : "))
num3=int(input("enter the 3rd number : "))
#count=0
num11=0
reply="y"
#int(num11)
##
##while count < 3:
##    if count< 3:
##        mul(num1,num2,num3)
##        
##        add(num1,num2,num3)
##        count=count+1
##    break
mul(num1,num2,num3)
#print("multiplication task Completed, thank you")
add(num1,num2,num3)
#print("Addition task Completed, thank you")



##
##
##-------------------------------------------------------------------OUTPUT--------------------------------------------
####= RESTART: C:\Komala Balakrishna\Python Scripts\AWS Practise Scripts\Assignement -20201113.py
##enter the first number : 0
##enter the 2nd number : 1
##enter the 3rd number : 2
##1st input is zero
##Do you wish to enter non-zero number : y/n ? ---> y
##please re-enter another non-zero number: 6
##
## 12 is the product of given numbers
##multiplication task Completed, thank you
##
## 9 is the sum of given numbers
##Addition task Completed, thank you
##>>> 
##= RESTART: C:\Komala Balakrishna\Python Scripts\AWS Practise Scripts\Assignement -20201113.py
##enter the first number : 1
##enter the 2nd number : 0
##enter the 3rd number : 3
##2nd input is zero
##Do you wish to enter non-zero number : y/n ? ---> y
##please re-enter another non-zero number: 4
##
## 12 is the product of given numbers
##multiplication task Completed, thank you
##
## 8 is the sum of given numbers
##Addition task Completed, thank you
##>>> 
##= RESTART: C:\Komala Balakrishna\Python Scripts\AWS Practise Scripts\Assignement -20201113.py
##enter the first number : 1
##enter the 2nd number : 2
##enter the 3rd number : 3
##
## 6 is the product of given numbers
##multiplication task Completed, thank you
##
## 6 is the sum of given numbers
##Addition task Completed, thank you
##>>> 
##= RESTART: C:\Komala Balakrishna\Python Scripts\AWS Practise Scripts\Assignement -20201113.py
##enter the first number : 0
##enter the 2nd number : 1
##enter the 3rd number : 3
##1st input is zero
##Do you wish to enter non-zero number : y/n ? ---> y
##please re-enter another non-zero number: 3
##
## 9 is the product of given numbers
##multiplication task Completed, thank you
##
## 7 is the sum of given numbers
##Addition task Completed, thank you
##>>> 
##= RESTART: C:\Komala Balakrishna\Python Scripts\AWS Practise Scripts\Assignement -20201113.py
##enter the first number : 3
##enter the 2nd number : 0
##enter the 3rd number : 2
##2nd input is zero
##Do you wish to enter non-zero number : y/n ? ---> y
##please re-enter another non-zero number: 3
##
## 18 is the product of given numbers
##multiplication task Completed, thank you
##
## 8 is the sum of given numbers
##Addition task Completed, thank you
##>>> 
##= RESTART: C:\Komala Balakrishna\Python Scripts\AWS Practise Scripts\Assignement -20201113.py
##enter the first number : 3
##enter the 2nd number : 3
##enter the 3rd number : 2
##
## 18 is the product of given numbers
##multiplication task Completed, thank you
##
## 8 is the sum of given numbers
##Addition task Completed, thank you
##>>> 
##= RESTART: C:\Komala Balakrishna\Python Scripts\AWS Practise Scripts\Assignement -20201113.py
##enter the first number : -0
##enter the 2nd number : 3
##enter the 3rd number : 4
##1st input is zero
##Do you wish to enter non-zero number : y/n ? ---> y
##please re-enter another non-zero number: 1
##
## 12 is the product of given numbers
##multiplication task Completed, thank you
##
## 8 is the sum of given numbers
##Addition task Completed, thank you
##>>> 
##
#
