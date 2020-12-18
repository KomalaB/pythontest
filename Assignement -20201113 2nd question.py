#provide sum and product of numbers provided count

def zero(n):
   if num1==0:
        print("1st input is zero")
        reply = input("Do you wish to enter non-zero number : y/n ? ---> "  )
        if reply=="y":
            num11=int(input("please re-enter another non-zero number: "))
            mul(num11,num2,num3)
            add(num11,num2,num3)
                #break
          #  return mul11+num2+num3
        
 
def mul(num1,num2,num3):
    if num1>0 and num2>0 and num3>0:
        mul1=num1*num2*num3
        print("\n", +mul1, "is the product of given numbers")
        print("multiplication task Completed, thank you")
               # return(mult1)
    elif num1==0 or num2==0 or num3==0:
        zero(num1,num2,num3)

        
def add(num1,num2,num3):
    if num1>0 and num2>0 and num3>0:
        addi=num1+num2+num3
        print("\n", +addi, "is the sum of given numbers")
        print("Addition task Completed, thank you")




count=int(input("Enter the number of variables")

num_list[1]: #define list
          
count1=count #set count value
          
while count1>0: 
    num=1
    num1=int(input("enter the ", +num," number : "))
    num_lsit.append(num1)
    num=num+1
    count1=count1-1
    
    if count==len(num_list):
        print("           Thank you for your inputs")
    break


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
