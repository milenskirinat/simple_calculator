import tkinter as tk
from unittest import result

root = tk.Tk()
root.title('Lyboe')
root.geometry('800x600')

def sum():
	result_output['text'] = int(input1.get()) + int(input2.get())

def minus():
	result_output['text'] = int(input1.get()) - int(input2.get())

input1 = tk.Entry(root)
input1.place(x = 10, y = 10)

btn_plus = tk.Button(root, text = '+', command = sum)
btn_plus.place(x = 10, y = 50)

btn_minus = tk.Button(root, text = '-', command = minus)
btn_minus.place(x = 70, y = 50)

input2 = tk.Entry(root)
input2.place(x = 10, y = 100)

result_output = tk.Label(root, text = "=")
result_output.place(x = 10, y = 150)

root.mainloop()