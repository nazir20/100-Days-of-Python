from tkinter import *


# calculate func
def calculate():
    entered_value = int(Input.get())
    km = entered_value * 1.6
    km = round(km)
    converted_value_label.config(text=f'{km}')


# window
window = Tk()
window.title('Mile to Km converter')
window.minsize(width=300, height=150)
window.config(padx=20, pady=40)

# Entry
Input = Entry()
Input.config(width=10)
Input.grid(column=1, row=0)

# mile label
mile_label = Label()
mile_label.config(text='Mile')
mile_label.grid(column=2, row=0)

# is equal to label
is_equal_to_label = Label()
is_equal_to_label.config(text='is equal to')
is_equal_to_label.grid(column=0, row=1)

# converted value label
converted_value_label = Label()
converted_value_label.config(text='0')
converted_value_label.grid(column=1, row=1)

# km label
km_label = Label()
km_label.config(text='Km')
km_label.grid(column=2, row=1)

# calculate button
calculate_btn = Button()
calculate_btn.config(text='Calculate', command=calculate)
calculate_btn.grid(column=1, row=2)
#
window.mainloop()
