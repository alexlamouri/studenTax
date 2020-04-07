import tkinter as tk
import tkinter.ttk as ttk
from Model import Model
from View import View

class Controller():

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("StudenTax")

        # mvc
        self.model = Model()
        self.view = View(self.root, self)

        self.root.mainloop()

    def switch_view(self, new_view):

        for old_view in self.view.views:
            self.view.views[old_view].grid_forget()

        self.view.views[new_view].grid(row=0, column=0)

    def calculate_return(self):
        pass

# mainloop
if __name__ == '__main__':
    c = Controller()