from tkinter import *
class MyWindow:
    def __init__(self,win):

        # Area for Title
        self.Title=Label(win,text="Calculator",fg="Red")
        self.Title.place(x=150, y=50)

        # Area for Number 1
        self.L1=Label(win, text="Number 1:", fg="Green")
        self.L1.place(x=50, y=80)
        self.E1=Entry(win, bd=2)
        self.E1.place(x=125, y=80)

        # Area for Number 2
        self.L2=Label(win, text="Number 2:", fg="Blue")
        self.L2.place(x=50, y=110)
        self.E2 = Entry(win, bd=2)
        self.E2.place(x=125, y=110)

        # Area for Results
        self.L3=Label(win, text="Result:", fg="Brown")
        self.L3.place(x=50, y=140)
        self.E3=Entry(win, bd=2)
        self.E3.place(x=125, y=140)

        # Buttons for Add and Subtract using BIND
        self.B1=Button(win, text="Add",fg="Gray")
        self.B1.place(x=80,y=200)
        self.B1.bind('<Button-1>', self.add)

        self.B2 = Button(win, text="Sub", fg="Gray")
        self.B2.place(x=120, y=200)
        self.B2.bind('<Button-1>', self.sub)
        # Buttons for Multiply and Divide without BIND
        self.B3 = Button(win, text="Mult", fg="Gray", command=self.mult)
        self.B3.place(x=160, y=200)

        self.B4 = Button(win, text="Div", fg="Gray", command=self.div)
        self.B4.place(x=200, y=200)

    def add(self,win):
        num1 = int(self.E1.get())
        num2 = int(self.E2.get())
        result = num1 + num2
        self.E3.delete(0, END)
        self.E3.insert(END, str(result))

    def sub(self,win):
        num1 = int(self.E1.get())
        num2 = int(self.E2.get())
        result = num1 - num2
        self.E3.delete(0, END)
        self.E3.insert(END, str(result))

    def mult(self):
        num1 = int(self.E1.get())
        num2 = int(self.E2.get())
        result = num1 * num2
        self.E3.delete(0, END)
        self.E3.insert(END, str(result))

    def div(self):
        num1 = int(self.E1.get())
        num2 = int(self.E2.get())
        result = num1 / num2
        self.E3.delete(0, END)
        self.E3.insert(END, str(result))


window = Tk()
MyWin = MyWindow(window)
window.configure(bg='Brown')
window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.mainloop()