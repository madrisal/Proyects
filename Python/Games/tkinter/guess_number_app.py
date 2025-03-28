import tkinter as tk
from random import randint

class GuessTheNumberApp:
    def __init__(self, root, max_value):
        self.root = root
        self.root.title("Think a Number")
        self.max_value = max_value
        self.lower_bound = 1
        self.upper_bound = max_value
        self.guess = None

        self.label = tk.Label(root, text=f"Think of a number between 1 and {self.max_value}.\nPress 'Start' to begin!")
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack(pady=10)

        self.guess_label = tk.Label(root, text="", font=("Arial", 16))
        self.guess_label.pack(pady=10)

        button_frame = tk.Frame(root)  
        button_frame.pack(pady=10)

        self.high_button = tk.Button(button_frame, text="Too High", command=self.too_high, state=tk.DISABLED, width=10)
        self.high_button.pack(side=tk.LEFT, padx=5)

        self.low_button = tk.Button(button_frame, text="Too Low", command=self.too_low, state=tk.DISABLED, width=10)
        self.low_button.pack(side=tk.LEFT, padx=5)

        self.correct_button = tk.Button(button_frame, text="Correct!", command=self.correct, state=tk.DISABLED, width=10)
        self.correct_button.pack(side=tk.LEFT, padx=5)

    def start_game(self):
        self.lower_bound = 1
        self.upper_bound = self.max_value
        self.make_guess()
        self.high_button.config(state=tk.NORMAL)
        self.low_button.config(state=tk.NORMAL)
        self.correct_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)

    def make_guess(self):
        if self.lower_bound != self.upper_bound:
            self.guess = randint(self.lower_bound, self.upper_bound)
        else:
            self.guess = self.lower_bound
        self.guess_label.config(text=f"My guess is: {self.guess}")

    def too_high(self):
        self.upper_bound = self.guess - 1
        self.make_guess()

    def too_low(self):
        self.lower_bound = self.guess + 1
        self.make_guess()

    def correct(self):
        self.guess_label.config(text=f"WoHoo! I guessed it! Your number is {self.guess}.")
        self.high_button.config(state=tk.DISABLED)
        self.low_button.config(state=tk.DISABLED)
        self.correct_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)


root = tk.Tk()
app = GuessTheNumberApp(root, 10)
root.mainloop()
