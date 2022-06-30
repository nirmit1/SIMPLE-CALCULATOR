import tkinter as tk

def add():
    num1 = int(box1.get())
    num2 = int(box2.get())
    result = num1 + num2
    box3.delete(0, tk.END)
    box3.insert(0, result)

def sub():
    num1 = int(box1.get())
    num2 = int(box2.get())
    result = num1 - num2
    box3.delete(0, tk.END)
    box3.insert(0, result)

def multiply():
    num1 = int(box1.get())
    num2 = int(box2.get())
    result = num1 * num2
    box3.delete(0, tk.END)
    box3.insert(0, result)

def divide():
    num1 = int(box1.get())
    num2 = int(box2.get())
    result = num1 / num2
    box3.delete(0, tk.END)
    box3.insert(0, result)

def clear():
    box1.delete(0, tk.END)
    box2.delete(0, tk.END)
    box3.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.iconbitmap("calc_logo.ico")
root.geometry("650x300")

label1 = tk.Label(root, text="NUMBER 1:", font = ("Arial", 20))
label1.place(x=20, y=20)

label2 = tk.Label(root, text="NUMBER 2:", font = ("Arial", 20))
label2.place(x=20, y=100)

label3 = tk.Label(root, text="RESULT: ", font = ("Arial", 20))
label3.place(x=20, y=180)

box1 = tk.Entry(root, font = ("Arial", 20))
box1.place(x=180, y=20)

box2 = tk.Entry(root, font = ("Arial", 20))
box2.place(x=180, y=100)

box3 = tk.Entry(root, font = ("Arial", 20))
box3.place(x=180, y=180)

button1 = tk.Button(root, text = "+", font=("Verdana",12), bg = "Cyan",command = add)
button1.place(x=180, y= 240, width = 50)

button2 = tk.Button(root, text = "*", font=("Verdana",12), bg = "Cyan",command = multiply)
button2.place(x=250, y= 240, width = 50)

button3 = tk.Button(root, text = "-", font=("Verdana",12), bg = "Cyan",command = sub)
button3.place(x=320, y= 240, width = 50)

button4 = tk.Button(root, text = "/ ", font=("Verdana",12), bg = "Cyan",command = divide)
button4.place(x=390, y= 240, width = 50)

button4 = tk.Button(root, text = "C ", font=("Verdana",12), bg = "Red",command = clear)
button4.place(x=460, y= 240, width = 50)

root.mainloop()
