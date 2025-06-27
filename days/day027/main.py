import tkinter as tk

font = ("Nunito", 14)

window = tk.Tk()

label_ieq = tk.Label(text="is equal to")
label_ieq.grid(column=0, row=1)

label_ieq = tk.Label(text="Miles")
label_ieq.grid(column=2, row=0)

label_ieq = tk.Label(text="Km")
label_ieq.grid(column=2, row=1)

entry_miles = tk.Entry()
entry_miles.grid(column=1, row=0)
entry_miles.configure(width=10)

label_converted_number = tk.Label()
label_converted_number.grid(column=1, row=1)


def on_button_clicked():
    label_converted_number["text"] = int(entry_miles.get()) * 1.609


convert_button = tk.Button(text="Convert", command=on_button_clicked)
convert_button.grid(column=1, row=2)


window.mainloop()
