import tkinter as tk
import random
import pyperclip as cb
import json
from tkinter import messagebox as mb

# ---------------------------- PASSWORD GENERATOR ---------------------#


def generate_password():
    lower_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    upper_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    numbers = [str(i) for i in range(10)]
    symbols = list("!@#$%^&*()-_=+[]{}|;:',.<>?/~`")

    list_lower_letters = [random.choice(lower_letters) for _ in range(2, 10)]
    list_upper_letters = [random.choice(upper_letters) for _ in range(2, 10)]
    list_numbers = [random.choice(numbers) for _ in range(2, 6)]
    list_symbols = [random.choice(symbols) for _ in range(2, 6)]

    all_chars = list_lower_letters + list_upper_letters + list_numbers + list_symbols
    random.shuffle(all_chars)
    password = ''.join(all_chars)
    cb.copy(password)

    return password


# ---------------------------- SAVE PASSWORD ------------------------- #

def save_password():
    if not mb.askokcancel(
            title="Confirmation",
            message="Do you want to save this password?"):
        return

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    with open("passwords.json", "w") as file:
        data.update(new_data)
        json.dump(data, file, indent=4)

    mb.showinfo(title="Operation Successful!",
                message="Your password was successfully saved!")
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------ #


window = tk.Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20)

# MyPass Logo
mypass_logo = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=mypass_logo)
canvas.grid(column=1, row=0)


# Left Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password")
password_label.grid(column=0, row=3)


# Entries
website_entry = tk.Entry(width=25)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = tk.Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "cs.daniel.sanso@gmail.com")

password_entry = tk.Entry(width=25)
password_entry.grid(column=1, row=3)


# Buttons
def on_generate_button_click():
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generate_password())


def on_add_button_click():
    save_password()


def on_search_button_click():
    try:
        website = website_entry.get()
        with open("passwords.json") as file:
            website_item = json.load(file)[website.title()]

        mb.showinfo(title="Website information",
                    message=f"The data for {website} is:\n"
                            f"Email: {website_item["email"]}\n"
                            f"Password: {website_item["password"]}")
        website_entry.delete(0, tk.END)

    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        mb.showwarning(title="Website not found.",
                       message="The website was not found!")


search_button = tk.Button(text="Search", width=16,
                          command=on_search_button_click)
search_button.grid(column=2, row=1)

generate_button = tk.Button(text="Generate Password",
                            command=on_generate_button_click)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=42,
                       command=on_add_button_click)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
