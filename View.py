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

        self.views = dict.fromkeys(["home", "t3", "t4", "t4a", "t4e", "t5", "t2202"])

        self.views["t3"] = self.init_t3_view(root)

        self.views["t4"] = self.init_t4_view(root)

        self.views["t4a"] = self.init_t4a_view(root)

        self.views["t4e"] = self.init_t4e_view(root)

        self.views["t5"] = self.init_t5_view(root)

        self.views["t2202"] = self.init_t2202_view(root)

        self.views["home"] = self.init_home_view(root)
        self.views["home"].grid(row=0,column=0)

        self.init_menu(root)

    def init_menu(self, root):

        self.main_menu = main_menu = tk.Menu(root)

        self.file_menu = file_menu = tk.Menu(main_menu, tearoff=0)

        self.add_menu = add_menu = tk.Menu(file_menu, tearoff=0)
        add_menu.add_command(label="Add T3 slip", command=lambda:self.switch_view('t3'))
        add_menu.add_command(label="Add T4 slip", command=lambda:self.switch_view('t4'))
        add_menu.add_command(label="Add T4A slip", command=lambda:self.switch_view('t4a'))
        add_menu.add_command(label="Add T4E slip", command=lambda:self.switch_view('t4e'))
        add_menu.add_command(label="Add T5 slip", command=lambda:self.switch_view('t5'))
        add_menu.add_command(label="Add T2202 slip", command=lambda:self.switch_view('t2202'))
        file_menu.add_cascade(label="Add tax slip", menu=add_menu)

        file_menu.add_command(label="View tax slips", state='disabled')
        file_menu.add_command(label="Calculate return", state='disabled')
        file_menu.add_command(label="Quit", command=lambda:root.quit())

        self.options_menu = options_menu = tk.Menu(main_menu, tearoff=0)

        self.themes_menu = themes_menu = tk.Menu(options_menu, tearoff=0)
        themes_menu.add_radiobutton(label="Light", value=1)
        themes_menu.add_radiobutton(label="Dark", state='disabled')
        options_menu.add_cascade(label="Change Themes", menu=themes_menu)

        self.fontfamily_menu = fontfamily_menu = tk.Menu(options_menu, tearoff=0)
        fontfamily_menu.add_radiobutton(label="Times New Roman")
        fontfamily_menu.add_radiobutton(label="Arial", state='disabled')
        fontfamily_menu.add_radiobutton(label="Calibri", state='disabled')
        options_menu.add_cascade(label="Change Font Family", menu=fontfamily_menu)

        self.fontsize_menu = fontsize_menu = tk.Menu(options_menu, tearoff=0)
        fontsize_menu.add_radiobutton(label="S")
        fontsize_menu.add_radiobutton(label="M", state='disabled')
        fontsize_menu.add_radiobutton(label="L", state='disabled')
        options_menu.add_cascade(label="Change Font Size", menu=fontsize_menu)

        self.help_menu = help_menu = tk.Menu(main_menu, tearoff=0)
        help_menu.add_command(label="About", state='disabled')
        help_menu.add_command(label="Instructions", state='disabled')

        main_menu.add_cascade(label="File", menu=file_menu)
        main_menu.add_cascade(label="Options", menu=options_menu)
        main_menu.add_cascade(label="Help", menu=help_menu)

        root.config(menu=main_menu)

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

    def switch_view(self, new_view):

        for view in self.views:
            self.views[view].grid_forget()

        self.views[new_view].grid(row=0, column=0)