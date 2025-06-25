import tkinter as tk
import time
import pygame
from threading import Thread

# ------------------ Settings ------------------
WORK_TIME = 25 * 60  # 25 minutes
SHORT_BREAK = 5 * 60  # 5 minutes
LONG_BREAK = 15 * 60  # 15 minutes
SESSIONS_BEFORE_LONG_BREAK = 4

# ------------------ Alarm Setup ------------------
pygame.mixer.init()
try:
    pygame.mixer.music.load("alaram.wav")
except pygame.error:
    print("Failed to load alaram.wav")


# ------------------ Main App ------------------
class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.session_count = 0
        self.running = False
        self.current_seconds = WORK_TIME

        self.label = tk.Label(root, text="Pomodoro Timer", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        self.timer_label = tk.Label(root, text="", font=("Courier", 36))
        self.timer_label.pack(pady=20)

        self.session_label = tk.Label(root, text="Session: Work", font=("Arial", 12))
        self.session_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, expand=True, padx=20, pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.RIGHT, expand=True, padx=20, pady=10)

        self.update_display()

    def update_display(self):
        mins, secs = divmod(self.current_seconds, 60)
        self.timer_label.config(text=f"{mins:02}:{secs:02}")

    def play_alarm(self):
        pygame.mixer.music.play()

    def start_timer(self):
        if not self.running:
            self.running = True
            Thread(target=self.countdown).start()

    def countdown(self):
        while self.current_seconds > 0 and self.running:
            time.sleep(1)
            self.current_seconds -= 1
            self.root.after(0, self.update_display)

        if self.running:
            self.play_alarm()
            self.session_count += 1
            self.root.after(0, self.next_session)

    def next_session(self):
        if self.session_count % (SESSIONS_BEFORE_LONG_BREAK * 2) == 0:
            self.current_seconds = LONG_BREAK
            self.session_label.config(text="Session: Long Break")
        elif self.session_count % 2 == 0:
            self.current_seconds = WORK_TIME
            self.session_label.config(text="Session: Work")
        else:
            self.current_seconds = SHORT_BREAK
            self.session_label.config(text="Session: Short Break")

        self.running = False
        self.update_display()

    def reset_timer(self):
        self.running = False
        self.session_count = 0
        self.current_seconds = WORK_TIME
        self.session_label.config(text="Session: Work")
        self.update_display()


# ------------------ Run App ------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
