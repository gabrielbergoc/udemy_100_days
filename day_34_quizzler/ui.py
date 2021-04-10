from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quizbrain = quizbrain
        self.window = self.make_window()

        self.score_label = self.make_score_label()

        self.canvas = self.make_canvas()
        self.canvas_text = self.make_canvas_text()

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, command=self.answer_true)
        self.true_button.grid(row=2, column=1, padx=20, pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, command=self.answer_false)
        self.false_button.grid(row=2, column=0, padx=20, pady=20)

        self.window.mainloop()


    def answer_true(self):
        is_correct = self.quizbrain.check_answer("true")
        self.feedback(is_correct)

    def answer_false(self):
        is_correct = self.quizbrain.check_answer("false")
        self.feedback(is_correct)

    def feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(ms=1000, func=self.update)

    def update(self):
        self.canvas.config(bg="white")
        if self.quizbrain.still_has_questions():
            self.score = self.quizbrain.score
            self.score_label.config(
                text=f"Score:"
                     f" {self.quizbrain.score}/"
                     f"{self.quizbrain.question_number}"
            )
            self.canvas.itemconfig(
                self.canvas_text,
                text=self.quizbrain.next_question()
            )
        else:
            self.score_label.config(
                text=f"Score: "
                     f"{self.quizbrain.score}/"
                     f"{self.quizbrain.question_number}"
            )
            self.canvas.itemconfig(
                self.canvas_text,
                text=f"You completed the quiz!\n\n"
                     f"Score: {self.quizbrain.score}/{self.quizbrain.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def make_window(self):
        window = Tk()
        window.title("Quizzler")
        window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR,
        )
        return window

    def make_score_label(self):
        label = Label(
            text=f"Score: {self.quizbrain.score}/{self.quizbrain.question_number}",
            fg="white",
            bg=THEME_COLOR,
            padx=20,
            pady=20,
            font=("Arial", 10, "normal"),
        )
        label.grid(row=0, column=1)

        return label

    def make_canvas(self):
        canvas = Canvas(
            width=300,
            height=300,
            bg="white",
        )
        canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        return canvas

    def make_canvas_text(self):
        canvas_text = self.canvas.create_text(
            150,
            150,
            text=self.quizbrain.next_question(),
            font=FONT,
            width=250,
            justify="center",
        )
        return canvas_text
