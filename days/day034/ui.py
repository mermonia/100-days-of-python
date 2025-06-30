import tkinter as tk
import time
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self._ui_setup()

    def _ui_setup(self):
        self.window = tk.Tk()
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.check_button_image = tk.PhotoImage(file="images/true.png")
        self.cross_button_image = tk.PhotoImage(file="images/false.png")
        self.check_button = tk.Button(image=self.check_button_image,
                                      command=self._on_check_button_clicked)
        self.cross_button = tk.Button(image=self.cross_button_image,
                                      command=self._on_cross_button_clicked)
        self.check_button.grid(column=0, row=2)
        self.cross_button.grid(column=1, row=2)
        self.is_button_on_cooldown = False

        self.update_ui()

        self.window.mainloop()

    def _on_cross_button_clicked(self):
        if self.is_button_on_cooldown:
            return
        self.check_answer("false")

    def _on_check_button_clicked(self):
        if self.is_button_on_cooldown:
            return
        self.check_answer("true")

    def check_answer(self, answer):
        self.is_button_on_cooldown = True
        if self.quiz.check_answer(answer):
            self.canvas.configure(bg="#33FF33")
        else:
            self.canvas.configure(bg="#FF3333")

        self.window.after(2000, self.display_next_question)

    def display_next_question(self):
        if self.quiz.still_has_questions():
            self.quiz.next_question()
            self.update_ui()
        else:
            self.end_quiz()
        self.is_button_on_cooldown = False

    def update_ui(self):
        self.canvas.configure(bg="white")
        self.canvas.itemconfigure(self.canvas_text,
                                  text=self.quiz.get_current_question_text())
        self.score_label.configure(text=f"Score: {self.quiz.score}")

    def end_quiz(self):
        self.canvas.configure(bg="white")
        self.canvas.itemconfigure(
                self.canvas_text,
                text="You finished the quiz! "
                f"Your final score was {self.quiz.score}/{self.quiz.question_number}."
        )
