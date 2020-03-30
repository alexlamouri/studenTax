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

        self.t4_view = self.init_t4_view(root)
        self.t4_view.grid(row = 0,column = 0)

    def init_home_view(self, root):

        view = tk.Frame(root, width = 500, height = 500)

        tk.Label(view, text = "Welcome to StudenTax").grid(row = 0, column  = 0)
        tk.Button(view, text = "Get Started").grid(row = 3, column = 0)

        return view

    def init_t4_view(self, root):

        view = tk.Frame(root)

        boxes = dict.fromkeys([14 , 16, 17, 18, 20, 22, 24, 26, 44, 46, 50, 52, 55, 56])

        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T4: Statement of Remuneration Paid").grid(row = 0, column = 0, columnspan = 8)
        tk.Label(title_frame, text = "Employer's Name").grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)

        i = 0
        box_frame = tk.Frame(view)
        for box in boxes:

            boxes[box] = []
            
            boxes[box].append(tk.Label(box_frame, text=box))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i // 8, column = i % 8)
            boxes[box][1].grid(row = i // 8, column= i % 8 + 1)

            i += 2

        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)

        return view