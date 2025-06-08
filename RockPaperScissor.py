import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("600x650")

        # Possible choices
        self.choices = ["Rock", "Paper", "Scissors"]
        # Scores
        self.user_score = 0
        self.comp_score = 0

        # Instruction label
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12))
        self.label.pack(pady=10)

        # Result display label
        self.result = tk.Label(root, text="", font=("Arial", 14), fg="blue")
        self.result.pack(pady=10)

        # Score display label
        self.score_label = tk.Label(root, text="You: 0 | Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Buttons for each choice
        for choice in self.choices:
            btn = tk.Button(root, text=choice, width=15,
                            command=lambda c=choice: self.play(c))
            btn.pack(pady=5)

    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        result_text = f"You chose {user_choice}, Computer chose {comp_choice}. "

        if user_choice == comp_choice:
            result_text += "It's a Draw!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result_text += "You Win! 🎉"
            self.user_score += 1
        else:
            result_text += "Computer Wins! 🤖"
            self.comp_score += 1

        # Update labels
        self.result.config(text=result_text)
        self.score_label.config(text=f"You: {self.user_score} | Computer: {self.comp_score}")

# Run the application
root = tk.Tk()
game = RPSGame(root)
root.mainloop()
