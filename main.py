import tkinter as tk


total_expression = ""
current_expression = "0"

root = tk.Tk()
root.geometry("375x667") #ukuran window
root.resizable(0, 0) # agar tidak bisa di maximaze
root.title("Calculator") #judul aplikasi
root.configure(background="black")

frame = tk.Frame(root, height=210, bg="#F5F5F5") 
frame.pack(expand=True, fill="both")

total_label= tk.Label(frame, text=total_expression, anchor=tk.E, bg="#F4F4F4", fg="#25265E", padx=24, font=("Arial", 16), wraplength=375, justify="right")
total_label.pack(expand=True, fill='both')

label = tk.Label(frame, text=current_expression, anchor=tk.E, bg="#F5F5F5", fg="#25265E", padx=24, font=("Arial", 40, "bold"), wraplength=375, justify="right")
label.pack(expand=True, fill='both')


btn_frame = tk.Frame(root)
btn_frame.pack(expand=True, fill="both")
btn_frame.rowconfigure(0, weight=1)

digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
real_oprator = ["/", "*" , "-", "+"]

def add_digit(digit):
    global current_expression
    if current_expression == "0" :
        current_expression = str(digit)
    elif current_expression == "Error":
        current_expression = str(digit)
    else:
        current_expression += str(digit)
    update_label()

def add_operator(operator):
    global current_expression
    global real_oprator
    if current_expression == "0" and operator == "-":
        current_expression = "-"
    elif current_expression[-1:] not in str(real_oprator) and operator in real_oprator:
        current_expression += operator
    update_label()

def clear():
    global current_expression
    global total_expression
    current_expression = "0"
    total_expression = ""
    total_label.config(text=total_expression)
    update_label()

def evaluate():
    global current_expression
    global total_expression
    global total_label
    expression = current_expression
    for operator, symbol in operations.items():
        expression = expression.replace(operator, f' {symbol} ')
    total_expression += expression
    total_label.config(text=total_expression)
    try:
        current_expression = str(eval(current_expression))
        total_expression = ""
    except Exception as e:
        total_expression = ""
        current_expression = "Error"
    finally:
        update_label()

def square():
    global current_expression
    current_expression = str(eval(f"{current_expression}**2"))
    update_label()
def delete():
    global current_expression
    current_expression = current_expression[:-1]
    if current_expression == "":
        current_expression = "0"
    update_label() 

def update_label():
    global label
    expression = current_expression
    for operator, symbol in operations.items():
        expression = expression.replace(operator, f' {symbol} ')
    label.config(text=expression)

for x in range(1, 5):
    btn_frame.rowconfigure(x, weight=1)
    btn_frame.columnconfigure(x, weight=1)


for digit, grid_value in digits.items():
    button = tk.Button(btn_frame, text=str(digit), bg="#ffffff", fg="#25265E", font=("Arial", 24,"bold"),borderwidth=0, command=lambda x=digit: add_digit(x))
    button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)


i = 0
for operator, symbol in operations.items():
    button = tk.Button(btn_frame, text=symbol, bg="#F8FAFF", fg="#25265E", font=("Arial", 20),
                        borderwidth=0, command=lambda x=operator: add_operator(x))
    button.grid(row=i, column=4, sticky=tk.NSEW)
    i += 1


button_clear = tk.Button(btn_frame, text="C", bg="#F8FAFF", fg="#25265E", font=("Arial", 20),
                           borderwidth=0, command=clear)
button_clear.grid(row=0, column=1, sticky=tk.NSEW)
button_equal = tk.Button(btn_frame, text="=", bg="orange", fg="#25265E", font=("Arial", 20),
                           borderwidth=0, command=evaluate)
button_equal.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
button_square = tk.Button(btn_frame, text="x\u00b2", bg="#F8FAFF", fg="#25265E", font=("Arial", 20),
                           borderwidth=0, command=square)
button_square.grid(row=0, column=2, sticky=tk.NSEW)
button_delete = tk.Button(btn_frame, text="\u232b", bg="#F8FAFF", fg="#25265E", font=("Arial", 20),borderwidth=0, command=delete)
button_delete.grid(row=0, column=3, sticky=tk.NSEW)

# bind return atinya untuk menghadle program ketika mengetik enter
root.bind("<Return>", lambda event: evaluate())
root.bind("<BackSpace>", lambda event: delete())

for key in digits:
    root.bind(str(key), lambda event, digit=key: add_to_expression(digit))
for key in operations:
    root.bind(key, lambda event, operator=key: append_operator(operator))

root.mainloop()