name=input("What is your name?\n")
print("Hello " + name)
print("Please answer all the questions to the best of your ability!\n")
q1=input("What days of the week do we start live reviews?\n")
q2=input("What is the full name of this class?\n")
score=0
if q1.lower() == "wednesday" or "wednesdays":
    score+=1
if q2.lower() == "computer science principles":
    score+=1
print(name + ", your score is: " + str(score) + "/2, or " + str(100*score/2) + " percent!")