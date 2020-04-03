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

        self.t3_view = self.init_t3_view(root)
        self.t4_view = self.init_t4_view(root)
        self.t4a_view = self.init_t4a_view(root)
        self.t4e_view = self.init_t4e_view(root)
        self.t5_view = self.init_t5_view(root)
        self.t2202_view = self.init_t2202_view(root)
        
        self.home_view.grid(row=0,column=0)

    def init_home_view(self, root):

        view = tk.Frame(root, width = 500, height = 500)

        tk.Label(view, text = "Welcome to StudenTax").grid(row = 0, column  = 0)
        tk.Button(view, text = "Get Started").grid(row = 3, column = 0)

        return view

    def init_t3_view(self, root):

        view = tk.Frame(root)

        boxes = dict.fromkeys([49, 50, 51, 21, 30, 23, 32, 39, 26, 48])

        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T3: Statement of Trust Income Allocations and Designations").grid(row = 0, column = 0, columnspan = 8)
        tk.Label(title_frame, text = "Trust's name").grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)

        i = 0
        box_frame = tk.Frame(view)
        for box in boxes:

            boxes[box] = []
            
            boxes[box].append(tk.Label(box_frame, text = box))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i // 8, column = i % 8)
            boxes[box][1].grid(row = i // 8, column= i % 8 + 1)

            i += 2

        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)

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
            
            boxes[box].append(tk.Label(box_frame, text = box))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i // 8, column = i % 8)
            boxes[box][1].grid(row = i // 8, column= i % 8 + 1)

            i += 2

        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)

        return view

    def init_t4a_view(self, root):

        view = tk.Frame(root)

        boxes = dict.fromkeys([16, 18, 20, 22, 24, 48])

        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T4A: Statement Of Pension, Retirement, Annuity And Other Income").grid(row = 0, column = 0, columnspan = 8)
        tk.Label(title_frame, text = "Name of payer").grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)

        i = 0
        box_frame = tk.Frame(view)
        for box in boxes:

            boxes[box] = []
            
            boxes[box].append(tk.Label(box_frame, text = box))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i // 8, column = i % 8)
            boxes[box][1].grid(row = i // 8, column= i % 8 + 1)

            i += 2

        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)

        return view

    def init_t4e_view(self, root):

        view = tk.Frame(root)

        boxes = dict.fromkeys([7, 14, 15, 17, 20, 21, 22, 23])

        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T4E: Statement of Employment Insurance").grid(row = 0, column = 0, columnspan = 8)

        i = 0
        box_frame = tk.Frame(view)
        for box in boxes:

            boxes[box] = []
            
            boxes[box].append(tk.Label(box_frame, text = box))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i // 8, column = i % 8)
            boxes[box][1].grid(row = i // 8, column= i % 8 + 1)

            i += 2

        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)

        return view

    def init_t5_view(self, root):

        view = tk.Frame(root)

        boxes = dict.fromkeys([24, 25, 26, 13, 18, 10, 11, 12])

        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T5: Statement of Investment Income").grid(row = 0, column = 0, columnspan = 8)
        
        tk.Label(title_frame, text = "Name of payer").grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)

        tk.Label(title_frame, text = "Exchange rate").grid(row = 2, column = 0, columnspan = 4)
        FloatEntry(title_frame).grid(row = 2, column = 4, columnspan = 8)

        i = 0
        box_frame = tk.Frame(view)
        for box in boxes:

            boxes[box] = []
            
            boxes[box].append(tk.Label(box_frame, text = box))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i // 8, column = i % 8)
            boxes[box][1].grid(row = i // 8, column= i % 8 + 1)

            i += 2

        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)

        return view
    
    def init_t2202_view(self, root):

        view = tk.Frame(root)

        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T2202: Tuition and Enrolment Certificate").grid(row = 0, column = 0, columnspan = 8)
        tk.Label(title_frame, text = "Institution name").grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)

        box_frame = tk.Frame(view)
        boxes = {}

        boxes["program"] = []
        boxes["program"].append(tk.Label(box_frame, text = "Program name"))
        boxes["program"].append(FloatEntry(box_frame))
        boxes["program"][0].grid(row = 0, column = 0)
        boxes["program"][1].grid(row = 1, column= 0)

        boxes["fees"] = []
        boxes["fees"].append(tk.Label(box_frame, text = "Program name"))
        boxes["fees"].append(FloatEntry(box_frame))
        boxes["fees"][0].grid(row = 0, column = 1)
        boxes["fees"][1].grid(row = 1, column= 1)

        boxes["pt"] = []
        boxes["pt"].append(tk.Label(box_frame, text = "Program name"))
        boxes["pt"].append(FloatEntry(box_frame))
        boxes["pt"][0].grid(row = 0, column = 2)
        boxes["pt"][1].grid(row = 1, column= 2)

        boxes["ft"] = []
        boxes["ft"].append(tk.Label(box_frame, text = "Program name"))
        boxes["ft"].append(FloatEntry(box_frame))
        boxes["ft"][0].grid(row = 0, column = 3)
        boxes["ft"][1].grid(row = 1, column= 3)

        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)

        return view
