print("Welcome to my computer quiz")

play = input("Do you want to play? (yes/no) ")

if play.lower() != "yes":
    quit()

print("Let's play...")
score = 0
count = 0
question = input("What does RAM stands for? ")
if question.lower() == "random access memory":
    print("It's correct")
    score += 1
else:
    print("Incorrect")
count += 1

question = input("What does CPU stands for? ")
if question.lower() == "central processing unit":
    print("It's correct")
    score += 1
else:
    print("Incorrect")
count += 1

question = input("What does GPU stands for? ")
if question.lower() == "graphical processing unit":
    print("It's correct")
    score += 1
else:
    print("Incorrect")
count += 1

question = input("What does ALU stands for? ")
if question.lower() == "arthimetic logic unit": 
    print("It's correct")
    score += 1
else:
    print("Incorrect")
count += 1

question = input("What does DBMS stands for? ")
if question.lower() == "database management system":
    score += 1
    print("It's correct")
else:
    print("Incorrect")
count += 1
# print("It's Correct",score +=1 if question.lower()== "database management system" else "InCorrect..!")--This code is done by MR Abhinav Gautam

print(f"You got {score} question correct out of {count} questions")
print(f"You got {(score / 5) * 100}%.")
