import tkinter as tk
import random

def check_guess():
    try:
        global attempts_left, score
        guess = int(guess_entry.get())
        attempts_left -= 1

        if guess < secret_number:
            result_label.config(text="Too low! Try a higher number.", fg="orange")
        elif guess > secret_number:
            result_label.config(text="Too high! Try a lower number.", fg="orange")
        else:
            score += attempts_left + 1
            result_label.config(text=f"Congratulations! You guessed the number ({secret_number}) in {max_attempts - attempts_left} attempts!", fg="green")
            update_score()
            submit_button.config(state=tk.DISABLED)
            guess_entry.config(state=tk.DISABLED)
            return

        if attempts_left == 0:
            result_label.config(text=f"Oops! You've reached the maximum attempts. The number was {secret_number}.", fg="red")
            update_score()
            submit_button.config(state=tk.DISABLED)
            guess_entry.config(state=tk.DISABLED)
            return

        attempts_label.config(text=f"Attempts left: {attempts_left}", fg="red")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.", fg="red")

def start_game():
    global secret_number, attempts_left, max_attempts, score
    secret_number = random.randint(1, 20)
    attempts_left = max_attempts
    attempts_label.config(text=f"Attempts left: {attempts_left}", fg="red")
    result_label.config(text="")
    submit_button.config(state=tk.NORMAL)
    guess_entry.config(state=tk.NORMAL)
    guess_entry.delete(0, tk.END)

def update_score():
    score_label.config(text=f"Score: {score}", fg="purple")

def set_difficulty(level):
    global max_attempts
    if level == "Easy":
        max_attempts = 8
    elif level == "Medium":
        max_attempts = 6
    else:
        max_attempts = 4
    start_game()

max_attempts = 5
secret_number = 0
attempts_left = max_attempts
score = 0

root = tk.Tk()
root.title("Enhanced Guessing Game")
root.geometry("500x450")

background_color = "#FDF7E4"  # Blue color
root.configure(bg=background_color)

title_label = tk.Label(root, text="Guess the Number!", fg="#BBAB8C", bg=background_color, font=("Comic Sans MS", 24))
title_label.pack(pady=10)

difficulty_frame = tk.Frame(root, bg=background_color)
difficulty_frame.pack()

level_label = tk.Label(difficulty_frame, text="Select Level:", font=("Comic Sans MS", 16), bg=background_color, fg="#BBAB8C")
level_label.grid(row=0, column=0, padx=10, pady=10)

easy_button = tk.Button(difficulty_frame, text="Easy", command=lambda: set_difficulty("Easy"), bg="lightblue", fg="black", relief=tk.GROOVE, font=("Comic Sans MS", 14))
easy_button.grid(row=0, column=1, padx=10, pady=10)

medium_button = tk.Button(difficulty_frame, text="Medium", command=lambda: set_difficulty("Medium"), bg="lightgreen", fg="black", relief=tk.GROOVE, font=("Comic Sans MS", 14))
medium_button.grid(row=0, column=2, padx=10, pady=10)

hard_button = tk.Button(difficulty_frame, text="Hard", command=lambda: set_difficulty("Hard"), bg="salmon", fg="black", relief=tk.GROOVE, font=("Comic Sans MS", 14))
hard_button.grid(row=0, column=3, padx=10, pady=10)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}", fg="#BBAB8C", font=("Comic Sans MS", 16), bg=background_color)
attempts_label.pack()

guess_entry = tk.Entry(root, font=("Comic Sans MS", 16))
guess_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit Guess", command=check_guess, font=("Comic Sans MS", 14))
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Comic Sans MS", 16), bg=background_color, fg="#BBAB8C")
result_label.pack()

score_label = tk.Label(root, text=f"Score: {score}", fg="#BBAB8C", font=("Comic Sans MS", 16), bg=background_color)
score_label.pack()

start_button = tk.Button(root, text="Start New Game", command=start_game, bg="#DED0B6", fg="black", relief=tk.GROOVE, font=("Comic Sans MS", 14))
start_button.pack(pady=20)

start_game()

root.mainloop()
