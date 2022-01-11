from tkinter import *
from playsound import playsound
# ---------------------------- CONSTANTS ------------------------------- #
BEIGE = "#fbe6c2"
RED = "#ac0d0d"
ORANGE = "#f48b29"
YELLOW = "#f0c929"
FONT_NAME = "Ink Free"
# ---------------------------- GLOBALS --------------------------------- #
timer = None
minutes = 5
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=RED)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    countdown(minutes * 60)
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
        canvas.itemconfig(timer_text, text="TOAST\nREADY! :D")
        playsound("Ring10.wav")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Toast Timer")
window.config(padx=50, pady=50, bg=BEIGE)

image = PhotoImage(file="bread-and-cheese-clipart-4-removebg-preview.png")

canvas = Canvas(width=500, height=500, bg=BEIGE, highlightthickness=0)
canvas.create_image(250, 250, image=image)
timer_text = canvas.create_text(250, 250, text="00:00", fill=RED, font=(FONT_NAME, 50, "bold"))
canvas.grid(row=1, column=1)

#labels
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=BEIGE, fg=RED)
timer_label.grid(row=0, column=1, pady=20)

#buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
    global minutes
    minutes = int(value)
scale = Scale(from_=10, to=1, command=scale_used)
scale.grid(row=2, column=1)

window.mainloop()
