# TASK-1) CALCULATOR --->
import tkinter as tk

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Simple Calculator")
    gui.geometry("300x400")

    expression = ""
    equation = tk.StringVar()

    entry_box = tk.Entry(gui, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14,
                         borderwidth=4)
    entry_box.grid(row=0, column=0, columnspan=4)

    button1 = tk.Button(gui, text=' 1 ', command=lambda: press(1), height=2, width=6)
    button1.grid(row=2, column=0)

    button2 = tk.Button(gui, text=' 2 ', command=lambda: press(2), height=2, width=6)
    button2.grid(row=2, column=1)

    button3 = tk.Button(gui, text=' 3 ', command=lambda: press(3), height=2, width=6)
    button3.grid(row=2, column=2)

    button4 = tk.Button(gui, text=' 4 ', command=lambda: press(4), height=2, width=6)
    button4.grid(row=3, column=0)

    button5 = tk.Button(gui, text=' 5 ', command=lambda: press(5), height=2, width=6)
    button5.grid(row=3, column=1)

    button6 = tk.Button(gui, text=' 6 ', command=lambda: press(6), height=2, width=6)
    button6.grid(row=3, column=2)

    button7 = tk.Button(gui, text=' 7 ', command=lambda: press(7), height=2, width=6)
    button7.grid(row=4, column=0)

    button8 = tk.Button(gui, text=' 8 ', command=lambda: press(8), height=2, width=6)
    button8.grid(row=4, column=1)

    button9 = tk.Button(gui, text=' 9 ', command=lambda: press(9), height=2, width=6)
    button9.grid(row=4, column=2)

    button0 = tk.Button(gui, text=' 0 ', command=lambda: press(0), height=2, width=6)
    button0.grid(row=5, column=0)

    plus = tk.Button(gui, text=' + ', command=lambda: press("+"), height=2, width=6)
    plus.grid(row=2, column=3)

    minus = tk.Button(gui, text=' - ', command=lambda: press("-"), height=2, width=6)
    minus.grid(row=3, column=3)

    multiply = tk.Button(gui, text=' * ', command=lambda: press("*"), height=2, width=6)
    multiply.grid(row=4, column=3)

    divide = tk.Button(gui, text=' / ', command=lambda: press("/"), height=2, width=6)
    divide.grid(row=5, column=3)

    equal = tk.Button(gui, text=' = ', command=equalpress, height=2, width=6)
    equal.grid(row=5, column=2)

    clear = tk.Button(gui, text='Clear', command=clear, height=2, width=6)
    clear.grid(row=5, column=1)

    Decimal = tk.Button(gui, text='.', command=lambda: press('.'), height=2, width=6)
    Decimal.grid(row=6, column=0)

    gui.mainloop()
