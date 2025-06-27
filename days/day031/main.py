import tkinter as tk
import pandas as pd
import random

# Constant and global definitions
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Nunito"
is_flipping_card = False

# ----------------- Flashcard Creation ---------------- #
# ---------------- and words management --------------- #

try:
    words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv("data/french_words.csv")
    print("No previous session found, starting new one!")
else:
    print("words_to_learn.csv file found, loaded previous session!")


def generate_new_word(language: str):
    global is_flipping_card

    language = language.title()
    chosen_word = random.choice(words[language].tolist())

    language_label.configure(text=language, bg="white", fg="black")
    word_label.configure(text=chosen_word, bg="white", fg="black")
    canvas.itemconfigure(canvas_image, image=flashcard_front_image)

    is_flipping_card = True
    window.after(3000, flip_card)


def flip_card():
    global is_flipping_card

    language_label.configure(text="English", bg="#91C2AF", fg="white")

    word_label.configure(
            text=words["English"][words["French"] == word_label.cget("text")].iloc[0],
            bg="#91C2AF", fg="white"
    )

    canvas.itemconfigure(canvas_image, image=flashcard_back_image)
    is_flipping_card = False


def remove_current_word():
    global words
    words = words[words["English"] != word_label.cget("text")]
    words.to_csv("data/words_to_learn.csv", index=False)


# --------------------- UI Setup ---------------------- #

window = tk.Tk()
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Main flashcard
flashcard_front_image = tk.PhotoImage(file="images/card_front.png")
flashcard_back_image = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
                   highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=flashcard_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# Labels
language_label = tk.Label(text="", font=(FONT_NAME, 30), bg="white")
language_label.place(x=400, y=150, anchor="center")

word_label = tk.Label(text="", font=(FONT_NAME, 40, "bold"), bg="white")
word_label.place(x=400, y=263, anchor="center")


# Buttons

def on_cross_button_clicked():
    if is_flipping_card:
        return
    generate_new_word("French")


def on_check_button_clicked():
    if is_flipping_card:
        return
    remove_current_word()
    generate_new_word("French")


cross_button_image = tk.PhotoImage(file="images/wrong.png")
check_button_image = tk.PhotoImage(file="images/right.png")

cross_button = tk.Button(image=cross_button_image, highlightthickness=0,
                         command=on_cross_button_clicked)
cross_button.grid(column=0, row=1)

check_button = tk.Button(image=check_button_image, highlightthickness=0,
                         command=on_check_button_clicked)
check_button.grid(column=1, row=1)

# Initial setup
generate_new_word("French")

window.mainloop()
