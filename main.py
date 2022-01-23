import requests 
import time
from tkinter import *
from requests.api import get

window = Tk()
window.title("Bitcoin Ticker")
window.config(padx=25, pady=25, bg='black')
window.geometry("400x400")

canvas = Canvas(width=298, height=300, bg='black', highlightthickness=0)
background_image = PhotoImage(file="bitcoin.png")
canvas.create_image(148, 148, image=background_image)
#price_text = canvas.create_text(150, 280, text="", width=250, font=("Arial", 30, "bold"), fill='white')
canvas.pack()

var = StringVar()
price_label = Label(textvariable=var, bg="black",fg="white", font=("Arial", 30, "bold"))
price_label.pack()


def get_price():
    #print("test")
    response = requests.get("https://api.coinstats.app/public/v1/coins/bitcoin?currency=US")
    response.raise_for_status()
    raw = response.json()
    data = raw['coin']
    price_data = "{:,}".format(round(data['price']))
    var.set(f"${price_data}")
    #canvas.itemconfig(price_text, text=f"${price_data}")
    window.after(2000, get_price)
   

window.after(1000, get_price)
window.mainloop()