# TASK-3) ROCK-PAPER-SCISSORS GAME --->
import tkinter as tk
from tkinter import messagebox
import random

user_score = 0
computer_score = 0
ties = 0

def game(user_choice):
    global user_score, computer_score, ties
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
        ties += 1
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    result_text = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}"
    result_label.config(text=result_text)
    scoreboard_label.config(text=f"Scoreboard - You: {user_score} Computer: {computer_score} Ties: {ties}")
    
    # Ask if the user wants to play again
    play_again()

def play_again():
    if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
        result_label.config(text="")
    else:
        messagebox.showinfo("Thank You!", "Thank you for playing!")
        root.quit()

def main():
    global root, result_label, scoreboard_label
    
    root = tk.Tk()
    root.title("Rock Paper Scissors")

    # Welcome message
    welcome_label = tk.Label(root, text="Welcome to Rock-Paper-Scissors Game!", font=("Helvetica", 16, "bold"))
    welcome_label.pack(pady=10)

    # Instructions
    instructions_label = tk.Label(root, text="Choose your weapon:", font=("Helvetica", 12))
    instructions_label.pack(pady=10)
    
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    
    tk.Button(button_frame, text="Rock", font=("Helvetica", 12), command=lambda: game("Rock")).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Paper", font=("Helvetica", 12), command=lambda: game("Paper")).grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="Scissors", font=("Helvetica", 12), command=lambda: game("Scissors")).grid(row=0, column=2, padx=10)
    
    result_label = tk.Label(root, text="", font=("Helvetica", 12), pady=10)
    result_label.pack()
    
    scoreboard_label = tk.Label(root, text="Scoreboard - You: 0 Computer: 0 Ties: 0", font=("Helvetica", 12), pady=10)
    scoreboard_label.pack()

    # Exit button
    tk.Button(root, text="Exit", font=("Helvetica", 12), command=root.quit).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
