from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
WORK_SECS = WORK_MIN * 60
SHORT_BREAK_MIN = 5
SHORT_BREAK_SECS = SHORT_BREAK_MIN * 60
LONG_BREAK_MIN = 20
LONG_BREAK_SECS = LONG_BREAK_MIN * 60
# ---------------------------- GLOBALS --------------------------------- #
repetitions = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global repetitions

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    repetitions = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetitions

    repetitions += 1

    if repetitions % 8 == 0:
        time = LONG_BREAK_SECS
        timer_label.config(text="Rest\na little\nmore :D", font=(FONT_NAME, 20, "bold"), fg=RED)
        timer_label.grid(row=0, column=1, pady=0)
    elif repetitions % 2 == 0:
        time = SHORT_BREAK_SECS
        timer_label.config(text="Rest\na little\nbit :)", font=(FONT_NAME, 20, "bold"), fg=PINK)
        timer_label.grid(row=0, column=1, pady=0)
    else:
        time = WORK_SECS
        timer_label.config(text="Work!", font=(FONT_NAME, 35, "bold"), fg=GREEN)
        timer_label.grid(row=0, column=1, pady=20)

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
        num_of_checkmarks = repetitions // 2
        checkmarks_label.config(text="✔" * num_of_checkmarks)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

image = PhotoImage(file="tomato.png")

canvas = Canvas(width=210, height=234, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 113, image=image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1)

#labels
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1, pady=20)

checkmarks_label = Label(bg=YELLOW, fg=GREEN)
checkmarks_label.grid(row=2, column=1)

#buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()