def add(a,b):
    return a+b
def sub(a,b):
    return a - b
def div(a,b):
    if b == 0:
        print("Error")
    else:
        return a/b
def mul(a,b):
    return a*b

print("1.add \n 2.sub\n 3.div\n 4.mul")

choice=int(input("Enter the options:"))

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))

if choice == 1:
    print("result:", add(num1,num2))
elif choice ==2:
    print("result:", sub(num1,num2))
elif choice == 3:
    print("result:", div(num1, num2))
elif choice == 4:
    print("result:", mul(num1, num2))
else:
    print("please add number:")





