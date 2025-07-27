import tkinter as tk


def press(num):
    current = expression.get()
    expression.set(current + str(num))


def equalpress():
    try:
        total = str(eval(expression.get()))
        expression.set(total)
    except:
        expression.set("Error")


def clear():
    expression.set("")


window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(0, 0)

expression = tk.StringVar()


entry = tk.Entry(window, textvariable=expression, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
    ('C',5,0)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=equalpress).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(window, text=text, padx=94, pady=20, font=('Arial', 14), command=clear).grid(row=row, column=col, columnspan=3)
    else:
        tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: press(t)).grid(row=row, column=col)


window.mainloop()
