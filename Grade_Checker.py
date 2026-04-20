name=input("Enter your name :")

Exam1=int(input("Enter your paper 1 mark :"))
Exam2=int(input("Enter your paper 2 mark :"))

Total= Exam1+Exam2
score= Total/2

if Exam1<=100 and not(Exam1<0) and Exam2<=100 and not(Exam2<0) :
       print(f"\nname : {name}")
       print(f"Total : {Total}/200")
       print(f"Percentage score :{int(score)}%")
       if score >=90 and score<=100:
        print("Grade :A")
       elif score >=80 and score <=89:
        print ("Grade :B")
       elif score >=70 and score <=79:
        print ("Grade :C")  
       elif score >=60 and score <=69:
        print ("Grade :D")
       elif score >=50 and score <=59:
        print ("Grade :E")
       else:
        print(" Grade :F")  
elif Exam1<0 or Exam2<0:
        print("mark cannot be below zero") 
else :
       print("mark cannot be above 100")


  


