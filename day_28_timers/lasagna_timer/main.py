from tkinter import *
from playsound import playsound
# ---------------------------- CONSTANTS ------------------------------- #
DARK_RED = "#8c0000"
RED = "#fa1e0e"
BRICK_RED = "#bd2000"
FONT_COLOR = "#f14668"
BACKGROUND_COLOR = "#ffd384"
FONT_NAME = "Gabriola"
HIGH_FIRE = 10 * 60
LOW_FIRE = 20 * 60
# ---------------------------- GLOBALS --------------------------------- #
timer = None
phases = 3
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global phases
    phases = 3

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=DARK_RED)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global phases

    if phases == 0:
        timer_label.config(text="Lasagna is ready 😋")
    elif phases % 2 == 0:
        time = LOW_FIRE
        timer_label.config(text="low fire 😇")
        phases -= 1
        countdown(time)
    elif phases % 2 != 0:
        time = HIGH_FIRE
        timer_label.config(text="HIGH FIRE!!! 😈")
        phases -= 1
        countdown(time)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer

    minutes = count // 60
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if minutes == 0:
        minutes = "00"
    if seconds < 10:
        seconds = f"0{seconds}"
    if seconds == 0:
        seconds = "00"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        playsound("Ring03.wav")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Lasagna Timer")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

image = PhotoImage(file="lasagne-clipart-7-removebg-preview.png")

canvas = Canvas(width=260, height=240, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(130, 120, image=image)
timer_text = canvas.create_text(130, 100, text="00:00", fill="white", font=(FONT_NAME, 46, "bold"))
canvas.grid(row=1, column=1)

#labels
timer_label = Label(text="Lasagna timer", font=(FONT_NAME, 35, "bold"), bg=BACKGROUND_COLOR, fg=DARK_RED)
timer_label.grid(row=0, column=1, pady=20)


#buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()