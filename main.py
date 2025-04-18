import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), justify='right')
        self.entry.pack(fill="both", padx=10, pady=10)

        buttonFrame = tk.Frame(master)
        buttonFrame.pack(fill="x", padx=10, pady=10)

        for i in range(4):
            buttonFrame.columnconfigure(i, weight=1)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(buttonFrame, text=text, font=("Arial", 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky="nsew")

        clear_button = tk.Button(master, text="C", font=("Arial", 18), command=self.clear)
        clear_button.pack(fill="x", padx=10)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Ошибка")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()