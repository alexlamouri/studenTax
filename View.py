import tkinter as tk
import tkinter.ttk as ttk

class FloatEntry(tk.Entry):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, validate="key")
        self.configure(validatecommand = (self.register(self.restrict),'%P','%d'))

    def restrict(self, val, act):
        if act == '1': # insert
            try:
                float(val)
            except:
                return False
            return True

class IntEntry(tk.Entry):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, validate="key")
        self.configure(validatecommand = (self.register(self.restrict),'%P','%d'))

    def restrict(self, val, act):
        if act == '1': # insert
            try:
                int(val)
            except:
                return False
            return True

class StrEntry(tk.Entry):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, validate="key")
        self.configure(validatecommand = (self.register(self.restrict),'%P','%d'))

    def restrict(self, val, act):
        if act == '1': # insert
            try:
                str(val)
            except:
                return False
            return True

class View():

    def __init__(self, root):

        # TODO switch view fcn
        self.home_view = self.init_home_view(root)
        self.home_view.grid(row = 0,column = 0) 

    def init_home_view(self, root):

        view = tk.Frame(root, width = 500, height = 500)

        tk.Label(view, text = "Welcome to StudenTax").grid(row = 0, column  = 0)
        tk.Button(view, text = "Get Started").grid(row = 3, column = 0)

        return view