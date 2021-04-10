import tkinter

# functions
def miles_to_km(miles):
    return miles / 0.62137119223733

def km_to_miles(km):
    return km * 0.62137119223733


#window
window = tkinter.Tk()
window.title("Distance converter")

# labels
label = tkinter.Label(text=f" = {miles_to_km(1)} Km")
label.grid(row=0, column=1)

# entries
entry = tkinter.Entry()
entry.insert(tkinter.END, string="1")
entry.grid(row=0, column=0)

#Radiobutton
def radio_used():
    radio_state.get()
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
miles_radio = tkinter.Radiobutton(text="mi", value=1, variable=radio_state, command=radio_used)
miles_radio.grid(row=1, column=0)
miles_radio.focus()
km_radio = tkinter.Radiobutton(text="Km", value=2, variable=radio_state, command=radio_used)
km_radio.grid(row=2, column=0)

# buttons
def button_clicked():
    option = radio_state.get()
    user_input = entry.get()
    if option == 1:
        answer = miles_to_km(float(user_input))
        label["text"] = " = " + str(answer) + " Km"
    elif option == 2:
        answer = km_to_miles(float(user_input))
        label["text"] = " = " + str(answer) + " mi"
    else:
        label["text"] = "Choose which unit you want to convert to"


button = tkinter.Button(text="Convert", command=button_clicked)
button.grid(row=1, column=1)


window.mainloop()