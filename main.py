from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_data = {}
words_to_learn = {}

try:
    data = pandas.read_csv("to_learn.csv")
except:
    data = pandas.read_csv("french_words.csv")
    current_data = data.to_dict(orient="records")
else:
    current_data = data.to_dict(orient="records")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# methods


def next_card():
    global current_data
    global words_to_learn
    global flip_timer
    window.after_cancel(flip_timer)
    words_to_learn = random.choice(current_data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{words_to_learn['French']}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{words_to_learn['English']}", fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)


def is_known():
    current_data.remove(words_to_learn)
    to_learn = pandas.DataFrame(current_data)
    to_learn.to_csv("to_learn.csv")

    next_card()


flip_timer = window.after(3000, func=flip_card)

# canvas


card_front_image = PhotoImage(file="card_front.png")
card_back_image = PhotoImage(file="card_back.png")
canvas = Canvas(width=800, height=536)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 48, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 68, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons

cross_image = PhotoImage(file="wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

tick_image = PhotoImage(file="right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=is_known)
tick_button.grid(column=1, row=1)

next_card()
window.mainloop()
