marks1=int(input("Enter your marks of English:"))
marks2=int(input("Enter your marks of Maths:"))
marks3=int(input("Enter your marks of Hindi:"))
marks4=int(input("Enter your marks of Science:"))

total=100*(marks1+marks2+marks3+marks4)/300
if(total>90 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print("ohhh!!!!!! you passed and also top!!") 

elif(total>40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print("You are passed,",total)
else:
    print("You are fail,try agin next year")




        


