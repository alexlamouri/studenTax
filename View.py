from tkinter import *
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

    def __init__(self, root, controller):

        self.controller = controller

        # init views
        self.views = dict.fromkeys(["home", "list", "t3", "t4", "t4a", "t4e", "t5", "t2202", "calculate_return"])
        self.views["home"] = self.init_home_view(root)
        self.views["list"] = self.init_list_view(root)
        self.views["t3"] = self.init_t3_view(root)
        self.views["t4"] = self.init_t4_view(root)
        self.views["t4a"] = self.init_t4a_view(root)
        self.views["t4e"] = self.init_t4e_view(root)
        self.views["t5"] = self.init_t5_view(root)
        self.views["t2202"] = self.init_t2202_view(root)
        self.views["calculate_return"] = self.init_calculate_return_view(root)

        self.views["home"].grid(row=0, column=0)

        # init menu
        self.init_menu(root)

    def init_menu(self, root):

        self.main_menu = main_menu = tk.Menu(root)

        self.file_menu = file_menu = tk.Menu(main_menu, tearoff=0)

        self.add_menu = add_menu = tk.Menu(file_menu, tearoff=0)
        add_menu.add_command(label="Add T3 slip", command=lambda:self.controller.switch_view('t3'))
        add_menu.add_command(label="Add T4 slip", command=lambda:self.controller.switch_view('t4'))
        add_menu.add_command(label="Add T4A slip", command=lambda:self.controller.switch_view('t4a'))
        add_menu.add_command(label="Add T4E slip", command=lambda:self.controller.switch_view('t4e'))
        add_menu.add_command(label="Add T5 slip", command=lambda:self.controller.switch_view('t5'))
        add_menu.add_command(label="Add T2202 slip", command=lambda:self.controller.switch_view('t2202'))
        file_menu.add_cascade(label="Add tax slip", menu=add_menu)

        file_menu.add_command(label="View tax slips", command=lambda:self.controller.switch_view('list'))
        file_menu.add_command(label="Calculate return", command=lambda:self.controller.switch_view('calculate_return'))
        file_menu.add_command(label="Quit", command=lambda:root.quit())

        self.options_menu = options_menu = tk.Menu(main_menu, tearoff=0)

        self.themes_menu = themes_menu = tk.Menu(options_menu, tearoff=0)
        themes_menu.add_radiobutton(label="Light", value=1)
        themes_menu.add_radiobutton(label="Dark", state='disabled')
        options_menu.add_cascade(label="Change Themes", menu=themes_menu)

        self.fontfamily_menu = fontfamily_menu = tk.Menu(options_menu, tearoff=0)
        fontfamily_menu.add_radiobutton(label="Times New Roman")
        fontfamily_menu.add_radiobutton(label="Arial")
        fontfamily_menu.add_radiobutton(label="Calibri")
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
        root.geometry("500x500")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        

        tk.Label(view, text = "Welcome to StudenTax", fg = 'midnight blue', font=("Helvetica", 16)).grid(row = 0, column  = 0, sticky="nsew")
        tk.Button(view, text = "Get Started", command=lambda:self.controller.switch_view('list'), fg = 'midnight blue', font=("Helvetica", 16)).grid(row = 3, column = 0)

        return view

    def init_t3_view(self, root):

        view = tk.Frame(root)


        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T3: Statement of Trust Income Allocations and Designations",font=("Helvetica", 16)).grid(row = 0, column = 0, columnspan = 8)
        tk.Label(title_frame, text = "Trust's name",font=("Helvetica", 16)).grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)


        box_frame = tk.Frame(view)
        boxes = dict.fromkeys([49, 50, 51, 21, 30, 23, 32, 39, 26, 48])
        i = 0
        for box in boxes:

            boxes[box] = []
            boxes[box].append(tk.Label(box_frame, text = box, fg = 'purple', font=("Helvetica", 15)))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i, column = 0)
            boxes[box][1].grid(row = i, column= 1)

            i += 1


        action_frame = tk.Frame(view)
        tk.Button(action_frame, text = "Clear", command=lambda: self.controller.clear(boxes)).grid(row=0, column=0, columnspan=4)
        tk.Button(action_frame, text = "Submit", command=lambda: self.controller.submit(('T3',boxes))).grid(row=0, column=4, columnspan=4)


        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)
        action_frame.grid(row=2, column=0)


        return view

    def init_t4_view(self, root):

        view = tk.Frame(root)

        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T4: Statement of Remuneration Paid", font=("Helvetica", 16)).grid(row = 0, column = 1, columnspan = 12)
        tk.Label(title_frame, text = "Employer's Name", font=("Helvetica", 16)).grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)


        box_frame = tk.Frame(view)
        boxes = dict.fromkeys([14 , 16, 17, 18, 20, 22, 24, 26, 44, 46, 50, 52, 55, 56])
        i = 0
        
        for box in boxes:
            boxes[box] = []
            boxes[box].append(tk.Label(box_frame, text = box, fg = 'red4', font=("Helvetica", 15)))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i, column = 0)
            boxes[box][1].grid(row = i, column= 1)

            i += 1


        action_frame = tk.Frame(view)
        tk.Button(action_frame, text = "Clear", command=lambda: self.controller.clear(boxes), font=("Helvetica", 15)).grid(row=0, column=0, columnspan=4)
        tk.Button(action_frame, text = "Submit", command=lambda: self.controller.submit(('T4',boxes), font=("Helvetica", 15))).grid(row=0, column=4, columnspan=4)


        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)
        action_frame.grid(row=2, column=0)


        return view

    def init_t4a_view(self, root):

        view = tk.Frame(root)


        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T4A: Statement Of Pension, Retirement, Annuity And Other Income", font=("Helvetica", 16)).grid(row = 0, column = 0, columnspan = 8)
        tk.Label(title_frame, text = "Name of payer", font=("Helvetica", 16)).grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)

        
        box_frame = tk.Frame(view)
        boxes = dict.fromkeys([16, 18, 20, 22, 24, 48])
        i = 0
        for box in boxes:
            boxes[box] = []
            boxes[box].append(tk.Label(box_frame, text = box, fg = 'chocolate3', font=("Helvetica", 15)))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i, column = 0)
            boxes[box][1].grid(row = i, column= 1)

            i += 1


        action_frame = tk.Frame(view)
        tk.Button(action_frame, text = "Clear", command=lambda: self.controller.clear(boxes), font=("Helvetica", 15)).grid(row=0, column=0, columnspan=4)
        tk.Button(action_frame, text = "Submit", command=lambda: self.controller.submit(('T4',boxes), font=("Helvetica", 15))).grid(row=0, column=4, columnspan=4)


        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)
        action_frame.grid(row=2, column=0)



        return view

    def init_t4e_view(self, root):

        view = tk.Frame(root)


        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T4E: Statement of Employment Insurance", font=("Helvetica", 16)).grid(row = 0, column = 0, columnspan = 8)

        
        box_frame = tk.Frame(view)
        boxes = dict.fromkeys([7, 14, 15, 17, 20, 21, 22, 23])
        i = 0
        for box in boxes:
            boxes[box] = []
            boxes[box].append(tk.Label(box_frame, text = box, fg = 'green', font=("Helvetica", 15)))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i, column = 0)
            boxes[box][1].grid(row = i, column= 1)

            i += 1


        action_frame = tk.Frame(view)
        tk.Button(action_frame, text = "Clear", command=lambda: self.controller.clear(boxes), font=("Helvetica", 15)).grid(row=0, column=0, columnspan=4)
        tk.Button(action_frame, text = "Submit", command=lambda: self.controller.submit(('T4',boxes), font=("Helvetica", 15))).grid(row=0, column=4, columnspan=4)


        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)
        action_frame.grid(row=2, column=0)



        return view

    def init_t5_view(self, root):

        view = tk.Frame(root)

        
        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T5: Statement of Investment Income", font=("Helvetica", 16)).grid(row = 0, column = 0, columnspan = 8)
        
        tk.Label(title_frame, text = "Name of payer").grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)

        tk.Label(title_frame, text = "Exchange rate").grid(row = 2, column = 0, columnspan = 4)
        FloatEntry(title_frame).grid(row = 2, column = 4, columnspan = 8)

        
        box_frame = tk.Frame(view)
        boxes = dict.fromkeys([24, 25, 26, 13, 18, 10, 11, 12])
        i = 0
        for box in boxes:
            boxes[box] = []
            boxes[box].append(tk.Label(box_frame, text = box, fg = 'firebrick4', font=("Helvetica", 15)))
            boxes[box].append(FloatEntry(box_frame))

            boxes[box][0].grid(row = i, column = 0)
            boxes[box][1].grid(row = i, column= 1)

            i += 1


        action_frame = tk.Frame(view)
        tk.Button(action_frame, text = "Clear", command=lambda: self.controller.clear(boxes), font=("Helvetica", 15)).grid(row=0, column=0, columnspan=4)
        tk.Button(action_frame, text = "Submit", command=lambda: self.controller.submit(('T4',boxes), font=("Helvetica", 15))).grid(row=0, column=4, columnspan=4)


        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)
        action_frame.grid(row=2, column=0)



        return view
    
    def init_t2202_view(self, root):

        view = tk.Frame(root)


        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "T2202: Tuition and Enrolment Certificate", font=("Helvetica", 16)).grid(row = 0, column = 0, columnspan = 8)
        tk.Label(title_frame, text = "Institution name").grid(row = 1, column = 0, columnspan = 4)
        StrEntry(title_frame).grid(row = 1, column = 4, columnspan = 8)


        box_frame = tk.Frame(view)
        boxes = {}
        boxes["program"] = []
        boxes["program"].append(tk.Label(box_frame, text = "Program name", fg = 'dark slate blue', font=("Helvetica", 15)))
        boxes["program"].append(FloatEntry(box_frame))
        boxes["program"][0].grid(row = 0, column = 0)
        boxes["program"][1].grid(row = 1, column= 0)

        boxes["fees"] = []
        boxes["fees"].append(tk.Label(box_frame, text = "Tuition fees", fg = 'dark slate blue', font=("Helvetica", 15)))
        boxes["fees"].append(FloatEntry(box_frame))
        boxes["fees"][0].grid(row = 0, column = 1)
        boxes["fees"][1].grid(row = 1, column= 1)

        boxes["pt"] = []
        boxes["pt"].append(tk.Label(box_frame, text = "Part-time months", fg = 'dark slate blue', font=("Helvetica", 15)))
        boxes["pt"].append(FloatEntry(box_frame))
        boxes["pt"][0].grid(row = 0, column = 2)
        boxes["pt"][1].grid(row = 1, column= 2)

        boxes["ft"] = []
        boxes["ft"].append(tk.Label(box_frame, text = "Full-time months", fg = 'dark slate blue', font=("Helvetica", 15)))
        boxes["ft"].append(FloatEntry(box_frame))
        boxes["ft"][0].grid(row = 0, column = 3)
        boxes["ft"][1].grid(row = 1, column= 3)


        action_frame = tk.Frame(view)
        tk.Button(action_frame, text = "Clear",command=lambda: self.controller.clear(boxes)).grid(row=0, column=0, columnspan=4)
        tk.Button(action_frame, text = "Submit", command=lambda: self.controller.submit(('T2202',boxes))).grid(row=0, column=4, columnspan=4)


        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)
        action_frame.grid(row=2, column=0)


        return view


    def init_list_view(self, root):

        view = tk.Frame(root)

        treeview = ttk.Treeview(view, columns=['slip', 'name'], selectmode='browse')
        treeview.heading('#0', text='')
        treeview.heading('slip', text='Tax Slip')
        treeview.heading('name', text='Name')
        treeview.grid(row=0,column=0)

        scrollbar = ttk.Scrollbar(view, orient=tk.VERTICAL, command=treeview.yview)
        treeview.configure(yscrollcommand=scrollbar.set) 
        scrollbar.grid(row=0, column=1, sticky='NSW')

        return view

    def init_calculate_return_view(self, root):
        eI = tk.StringVar()
        eIn = tk.StringVar()
        totIn = tk.StringVar()
        netIn = tk.StringVar()
        bpa = tk.StringVar()
        tP = tk.StringVar()
        tRC = tk.StringVar()
        r = tk.StringVar()
        self.data = [eI, eIn, totIn, netIn, bpa, tP, tRC, r] 

        view = tk.Frame(root)

        title_frame = tk.Frame(view)
        tk.Label(title_frame, text = "Calculate Return/Balance Owing", font=("Helvetica", 16)).grid(row = 0, column = 0, columnspan=8)
        
        box_frame = tk.Frame(view)
        boxes = dict.fromkeys([10100, 11900, 15000, 23600, 30000, 35000, 48200, 48400])
        labels = ['Employment Income', 'Employment Insurance', 'Total Income', 'Net Income',
                  'Basic Personal Amount', 'Total Payable', 'Total Refundable Credits', 'Refund']

        i = 0
        j = 0 
        
        for box in boxes:
            boxes[box] = []
            boxes[box].append(tk.Label(box_frame, text = box, fg = 'dark slate blue', font=("Helvetica", 15)))
            boxes[box].append(tk.Label(box_frame, text = labels[j], fg = 'dark slate blue', font=("Helvetica", 15)))
            boxes[box].append(tk.Label(box_frame, textvariable = self.data[j], fg = 'dark slate blue', font=("Helvetica", 15)))
            

            boxes[box][0].grid(row = i, column = 0)
            boxes[box][1].grid(row = i , column= 1)
            boxes[box][2].grid(row = i, column = 2)

            j += 1

            i += 1

        action_frame = tk.Frame(view)
        tk.Button(action_frame, text = "Calculate Returns", command = self.get_returns).grid(row= 10, column = 0, columnspan = 4)
        tk.Button(action_frame, text = "View my tax documents").grid(row = 10, column = 5, columnspan=4)
        tk.Button(action_frame, text = "Export to csv").grid(row=10, column = 10, columnspan=4)

        title_frame.grid(row=0, column=0)
        box_frame.grid(row=1, column=0)
        action_frame.grid(row=2, column=0)
        

        return view

    def get_returns(self):
        all_data = self.controller.calculate_return()

        j = 0 
        for line in self.data:
            line.set(all_data[j])
            j+= 1
        
        

    
