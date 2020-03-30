import tkinter as tk
import tkinter.ttk as ttk
from Model import Model
from View import View

class Controller():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("StudenTax")

        self.model = Model()
        self.view = View(self.root)
        self.root.mainloop()

if __name__ == '__main__':
    c = Controller()