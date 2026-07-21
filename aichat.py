# import pyautogui
# import openai

# while True:
#     a = pyautogui.position()
#     print(a)
import tkinter as tk
import random

# Mapping for choices
dictionary = {"s": 1, "p": -1, "sr": 0}
reversedDict = {-1: "Paper", 0: "Scissor", 1: "Stone"}

# Function to run the game logic
def play_game(user_choice):
    computer_choice = random.choice([-1, 0, 1])
    user_value = dictionary[user_choice]
    computer_value = computer_choice
    user_choice_text = reversedDict[user_value]
    computer_choice_text = reversedDict[computer_value]

    result = ""
    if computer_value == user_value:
        result = "It's a draw!"
    elif (computer_value == -1 and user_value == 0) or (computer_value == 1 and user_value == -1) or (computer_value == 0 and user_value == 1):
        result = "You Win!"
    else:
        result = "You Lose!"

    # Update the labels with the result and choices
    result_label.config(text=result)
    user_label.config(text=f"You chose: {user_choice_text}")
    computer_label.config(text=f"Computer chose: {computer_choice_text}")

# Function triggered by button clicks
def on_button_click(choice):
    play_game(choice)

# Set up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Instructions label
instructions_label = tk.Label(root, text="Choose: Stone (s), Paper (p), or Scissor (sr)", font=("Arial", 14))
instructions_label.pack(pady=10)

# User input buttons
stone_button = tk.Button(root, text="Stone (s)", width=20, command=lambda: on_button_click("s"))
stone_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper (p)", width=20, command=lambda: on_button_click("p"))
paper_button.pack(pady=5)

scissor_button = tk.Button(root, text="Scissor (sr)", width=20, command=lambda: on_button_click("sr"))
scissor_button.pack(pady=5)

# Labels to display the results and choices
user_label = tk.Label(root, text="You chose: ", font=("Arial", 12))
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Result will appear here.", font=("Arial", 14))
result_label.pack(pady=20)

# Run the application
root.mainloop()
