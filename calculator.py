#Calculator

#Function for Addition
def add(x,y):
    return x+y
#Function For Substraction
def sub(x,y):
    return x-y
#Function for Multiplication
def mul(x,y):
    return x*y
#Function for Divide
def div(x,y):
    return x/float(y)

print("Please Enter Your Selection")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")

#Taking input from user
choice= input("Enter choice(1/2/3/4): ")

num1 =int(input("Enter First Number:  "))
num2 =int(input("Enter Second Number: "))

if choice==1:
    print(num1,"+",num2,"=",add(num1,num2))

elif choice==2:
    print(num1,"-",num2,"=",sub(num1,num2))

elif choice==3:
    print(num1,"*",num2,"=",mul(num1,num2))

elif choice==4:
    print(num1,"/",num2,"=",div(num1,num2))

else:
    print("Invalid Choice")

