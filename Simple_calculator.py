print("This is a simple calculator that performs simple calculations\nIt uses basic operators +,-,* and / ,to add, subtract,multiply and divide respectively \n 1.You enter your first number \n 2.You select the operation you want to use \n.3 You enter the second number \n4.You press enter then you get an answer ")
print()

a=float(input("Enter the number :"))
c=input("enter the operator (+,-,*,/):")
b=float(input("Enter the number :"))

if c=="+" :
  print(f" answer : {a+b}")
elif c=="-" :
  print(f" answer : {a-b}")
elif c=="*" :
  print(f" answer : {a*b}")
elif c=="/" :
  if b==0:
   print("not applicable")
  else:
    print(f" answer : {a/b}")
else :
  print("invalid operator")