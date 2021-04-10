# ---------------- IMPORTS -------------- #
import pandas
import random
import tkinter.ttk as tkk
from tkinter import *

# ---------------- CONSTANTS ------------ #
BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Segoe Print", 12, "bold")

# ---------------- DATA MANAGEMENT ------ #
data = pandas.read_csv("data/fr_pt.csv")
data = data.to_dict(orient="records")

# ---------------- VARIABLES ------------ #
correct_answers = 0
wrong_answers = 0
current_word = random.choice(data)

# ---------------- FUNCTIONS ------------ #
def change_word():
    global current_word

    current_word = random.choice(data)
    canvas.itemconfig(image, image=card_front_img)
    canvas.itemconfig(language, text="Francês", fill="black")
    canvas.itemconfig(word, text=current_word["Francês"], fill="black")

def right_answer():
    global correct_answers

    correct_answers += 1
    correct_answers_label.config(text=f"Acertos: {correct_answers}")
    change_word()

def wrong_answer():
    global wrong_answers

    wrong_answers += 1
    wrong_answers_label.config(text=f"Erros: {wrong_answers}")
    change_word()

def flip():
    canvas.itemconfig(image, image=card_back_img)
    canvas.itemconfig(language, text="Português", fill="white")
    canvas.itemconfig(word, text=current_word["Português"], fill="white")

# ---------------- GUI ------------------ #
# window
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")
flip_button_img = PhotoImage(file="images/flip.png")

# canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="Francês", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=current_word["Francês"], font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

# buttons
right_button = Button(image=right_button_img, highlightthickness=0, command=right_answer)
right_button.grid(row=1, column=2)

wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=wrong_answer)
wrong_button.grid(row=1, column=0)

flip_button = Button(image=flip_button_img, highlightthickness=0, command=flip)
flip_button.grid(row=1, column=1)

# labels
correct_answers_label = Label(text="Acertos: 0", font=FONT, bg=BACKGROUND_COLOR)
correct_answers_label.grid(row=2, column=2)

wrong_answers_label = Label(text="Erros: 0", font=FONT, bg=BACKGROUND_COLOR)
wrong_answers_label.grid(row=2, column=0)


change_word()

window.mainloop()