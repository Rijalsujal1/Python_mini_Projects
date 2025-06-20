import tkinter as tk
import random
import time
import operator
from tkinter import messagebox

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul}

MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


class MathGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🧮 Timed Math Challenge")
        self.master.geometry("400x300")

        self.question_label = tk.Label(master, text="", font=("Arial", 20))
        self.question_label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Arial", 16))
        self.entry.pack()
        self.entry.bind("<Return>", self.check_answer)

        self.feedback = tk.Label(master, text="", font=("Arial", 14))
        self.feedback.pack(pady=10)

        self.status = tk.Label(master, text="", font=("Arial", 12))
        self.status.pack(pady=5)

        self.restart_button = tk.Button(master, text="Restart", command=self.start_game)
        self.restart_button.pack(pady=10)

        self.start_game()

    def generate_problem(self):
        left = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
        op = random.choice(list(OPS.keys()))
        answer = OPS[op](left, right)
        return f"{left} {op} {right}", answer

    def start_game(self):
        self.correct = 0
        self.total = 0
        self.start_time = time.time()
        self.next_question()

    def next_question(self):
        if self.total == TOTAL_PROBLEMS:
            total_time = round(time.time() - self.start_time, 2)
            avg_time = round(total_time / TOTAL_PROBLEMS, 2)
            messagebox.showinfo(
                "Game Over",
                f"✅ Correct: {self.correct}/{TOTAL_PROBLEMS}\n⏱️ Time: {total_time}s (avg {avg_time}s/question)",
            )
            return
        self.expr, self.answer = self.generate_problem()
        self.question_label.config(text=f"Problem #{self.total + 1}: {self.expr} = ?")
        self.entry.delete(0, tk.END)
        self.feedback.config(text="")
        self.status.config(text=f"Correct: {self.correct}/{self.total}")
        self.total += 1

    def check_answer(self, event):
        try:
            guess = int(self.entry.get())
            if guess == self.answer:
                self.feedback.config(text="✅ Correct!", fg="green")
                self.correct += 1
            else:
                self.feedback.config(
                    text=f"❌ Wrong! Correct was {self.answer}", fg="red"
                )
        except ValueError:
            self.feedback.config(text="⚠️ Enter a valid number", fg="orange")
        self.master.after(1000, self.next_question)


root = tk.Tk()
app = MathGame(root)
root.mainloop()
