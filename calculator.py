import tkinter as tk

window = tk.Tk()
window.title("Calculator")

input_string = tk.StringVar(value='')

input_box = tk.Entry(window, textvariable=input_string)
input_box.pack()

def append_operator(operator):
    input_string.set(input_string.get() + operator)

def evaluate():
    result = str(eval(input_string.get()))
    input_string.set(result)

def clear():
    input_string.set('')

plus_button = tk.Button(window, text='+', command=lambda: append_operator('+'))

minus_button = tk.Button(window, text='-', command=lambda: append_operator('-'))
multiply_button = tk.Button(window, text='*', command=lambda: append_operator('*'))
divide_button = tk.Button(window, text='/', command=lambda: append_operator('/'))

equals_button = tk.Button(window, text='=', command=evaluate)

clear_button = tk.Button(window, text='Clear', command=clear)

plus_button.pack(side='left')
minus_button.pack(side='left')
multiply_button.pack(side='left')
divide_button.pack(side='left')
equals_button.pack(side='left')
clear_button.pack(side='left')

window.mainloop()
