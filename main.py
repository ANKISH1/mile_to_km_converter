from tkinter import *

def get_km():
    miles = float(entry.get())
    km = miles * 1.609
    label3.config(text=f"{km}")



window = Tk()
window.title("Mile to Km Converter")
window.minsize(width= 600, height=400)
window.config(padx=200,pady=50)

entry = Entry(width=10)
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=3, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1,row=1)

label4 = Label(text="Km")
label4.grid(column=3, row=1)

button = Button(text="Calculate", command=get_km)
button.grid(column=1, row=3)























window.mainloop()