marks =  int(input("Enter the Marks : "))
passMarks=40;

if(marks < passMarks):
    print("Bettter luck next time ")
     
elif(marks > passMarks and marks < 50):
    print("Successfully complted with grade C")
elif(marks > 50 and marks <70):
    print("Successfully complted with grade.... B")
elif(marks > 70 and marks <80):
    print("Successfully complted with grade A")
elif(marks > 90 and marks <100):
    print("Successfully complted with grade S")


else:
     print("Over Graduate")


