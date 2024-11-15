from tkinter import *
import requests

window = Tk()
window.title("test")
window.config(padx=50, pady=50)


quote = Label(text = "")
quote.grid(row=0, column=0)

def generatenewquote():
    response = requests.get("https://zenquotes.io/api/random")
    response.raise_for_status()
    data = response.json()
    quote["text"] = data[0]["q"]
#quote["text"] = 


newquote = Button(text="new quote", command=generatenewquote)
newquote.grid(row=1, column=0)

generatenewquote()


window.mainloop()