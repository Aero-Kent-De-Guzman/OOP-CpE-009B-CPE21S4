import tkinter as tk
import math

# Functions for calculation

def add():
    output = float(entry1.get()) + float(entry2.get())
    result.set(output)
    entry3.insert(tk.END, f"{entry1.get()} + {entry2.get()} = {output}\n")
def subtract():
    output = float(entry1.get()) - float(entry2.get())
    result.set(output)
    entry3.insert(tk.END, f"{entry1.get()} - {entry2.get()} = {output}\n")
def multiply():
    output = float(entry1.get()) * float(entry2.get())
    result.set(output)
    entry3.insert(tk.END, f"{entry1.get()} x {entry2.get()} = {output}\n")
def divide():
    try:
        output = float(entry1.get()) / float(entry2.get())
        result.set(output)
        entry3.insert(tk.END, f"{entry1.get()} / {entry2.get()} = {output}\n")
    except ZeroDivisionError:
        result.set("Error! Division by zero.")
def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")
def power():
    output = float(pow(float(entry1.get()), float(entry2.get())))
    result.set(output)
    entry3.insert(tk.END, f"{entry1.get()} ^ {entry2.get()} = {output}\n")

def squareRoot():
    output = float(math.sqrt(float(entry1.get())))
    result.set(output)
    entry3.insert(tk.END, f"sqrt {entry1.get()} = {output}\n")

def sine():
    output = float(math.sin(float(entry1.get())))
    result.set(output)
    entry3.insert(tk.END, f"sine {entry1.get()} = {output}\n")

def cosine():
    output = float(math.cos(float(entry1.get())))
    result.set(output)
    entry3.insert(tk.END, f"cosine {entry1.get()} = {output}\n")


root = tk.Tk()
root.title("Simple Calculator")

result = tk.StringVar()

tk.Label(root, text="Enter first number:", bg="darkgray").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:", bg="darkgray").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="History:", bg="darkgray", font=("Arial", 12, "bold")).grid(row=0, column=2)
entry3 = tk.Text(root, width=10, height=5,wrap=tk.WORD)
entry3.grid(row=1, column=2)

tk.Button(root, text="Add", command=add, bg="red", font=("Arial", 12, "bold")).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract, bg="green", font=("Arial", 12, "bold")).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply, bg="yellow", font=("Arial", 12, "bold")).grid(row=3, column=0)
tk.Button(root, text="Divide", command=divide, bg="blue", font=("Arial", 12, "bold")).grid(row=3, column=1)

#pow button
tk.Button(root, text="a^b", command=power, bg="cyan", font=("Arial", 12, "bold")).grid(row=4, column=0)
#sqrt button
tk.Button(root, text="sqrt(a)", command=squareRoot, bg="brown", font=("Arial", 12, "bold")).grid(row=4, column=1)
#sine button
tk.Button(root, text="sin(a)", command=sine, bg="pink", font=("Arial", 12, "bold")).grid(row=5, column=0)
#cos button
tk.Button(root, text="cos(a)", command=cosine, bg="orange", font=("Arial", 12, "bold")).grid(row=5, column=1)
#clear button
tk.Button(root, text="Clear", command=clear, bg="white", font=("Arial", 12, "bold")).grid(row=6, column=0)



tk.Label(root, text="Result:", bg="darkgray").grid(row=7, column=0)
result_label = tk.Label(root, textvariable=result, bg="darkgray", font=("Arial", 12, "bold"))
result_label.grid(row=7, column=1)

root.configure(bg="darkgray")

root.mainloop()