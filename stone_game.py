'''
1 for stone
-1 for paper
0 for scissor
'''

import random

computer = random.choice([-1, 0, 1])
dictionary = {"s" : 1, "p" : -1, "sr" : 0}
reversedDictionary = {1 : "Stone", -1 : "Paper", 0 : "Scissor"}
while True:
    your = input("Enter your choice : ").lower()

    if your not in dictionary:
        print("Invalid choice!")

    else:
        you = dictionary[your]

        print(f"You chose {reversedDictionary[you]}\nComputer chose {reversedDictionary[computer]}")

        if(computer == you):
            print("Its a draw")
        elif(computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
                print("You Win!")
        else:
             print("You Lose!")
        break
        