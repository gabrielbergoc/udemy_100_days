# ---------------------------- IMPORTS ----------------------------------- #
from tkinter import *
from tkinter import messagebox
import random, pyperclip, json
# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Arial", 10, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_chars = [random.choice(letters) for i in range(nr_letters)] \
                     + [random.choice(symbols) for j in range(nr_symbols)] \
                     + [random.choice(numbers) for k in range(nr_numbers)]

    random.shuffle(password_chars)

    password = "".join(password_chars)

    password_entry.delete(0, END)
    password_entry.insert(END, string=password)

    pyperclip.copy(text=password)
    messagebox.showinfo(message="Password copied to the clipboard")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Don't leave any fields empty!")

    else:
        new_data = {
            website: {
                "username": username,
                "password": password
            }
        }

        try:
            # read pre-existing data
            with open("data.json", mode="r") as file:
                data = json.load(file)

        except FileNotFoundError:
            # dump data into json file
            with open("data.json", mode="w") as file:
                json.dump(obj=new_data, fp=file, indent=4)

        else:
            # update with new data
            data.update(new_data)

            # dump updated data into json file
            with open("data.json", mode="w") as file:
                json.dump(obj=data, fp=file, indent=4)

        finally:
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)
# ---------------------------- SEARCH FUNCTION ---------------------------- #
def search():

    website = website_entry.get()

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Not found", message="Login informations not found.")
    else:
        if website in data:
            username = data[website]['username']
            password = data[website]['password']

            pyperclip.copy(password)

            messagebox.showinfo(title=f"{website} login info",
                                message=f"Username: {username}\n\n"
                                        f"Password: {password}\n"
                                        f"(password copied to clipboard)")
        else:
            messagebox.showerror(title="Not found", message="Login informations not found.")
# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=200, height=189)
canvas.grid(row=0, column=0, columnspan=3)

# image
image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=image)

# labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0, sticky=(E))

username_label = Label(text="Email/Username:", font=FONT)
username_label.grid(row=2, column=0, sticky=(E))

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0, sticky=(E))

# entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky=(W))
website_entry.focus()

username_entry = Entry(width=42)
username_entry.insert(END, string="gabriel_cb17@hotmail.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky=(W))

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=(W))

# buttons
passwordgen_button = Button(text="Generate Password", width=16, command=password_generator)
passwordgen_button.grid(row=3, column=2, sticky=(W))

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=(W))

search_button = Button(text="Search", width=16, command=search)
search_button.grid(row=1, column=2, sticky=(W))


window.mainloop()