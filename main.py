from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# methods


def next_card():
    with open("french_words.csv", mode="r") as file:
        data = pandas.read_csv(file)
        data = data.to_dict(orient="records")
        current_data = random.choice(data)
        canvas.itemconfig(card_title, text="French")
        canvas.itemconfig(card_word, text=f"{current_data['French']}")

# canvas


card_front_image = PhotoImage(file="card_front.png")
canvas = Canvas(width=800, height=536)
canvas.create_image(400, 263, image=card_front_image)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 48, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 68, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons

cross_image = PhotoImage(file="wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)


tick_image = PhotoImage(file="right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=next_card)
tick_button.grid(column=1, row=1)


window.mainloop()