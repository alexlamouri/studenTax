import tkinter as tk
import tkinter.ttk as ttk
import Model as m
from View import View as v
from tkinter import filedialog

class Controller():

    def __init__(self):
        self.num_slips = 0

        self.file = 'StudenTax.csv'

        self.root = tk.Tk()
        self.root.title("StudenTax")

        # mvc
        self.model = m.CSVModel(self.file)
        self.view = v(self.root, self)

        self.root.mainloop()

    def switch_view(self, new_view):

        for old_view in self.view.views:
            self.view.views[old_view].grid_forget()
        
        self.view.views[new_view].grid(row=0, column=0)

    def clear(self, boxes):
        for box in boxes:
            boxes[box][1].delete(0,'end')

    def submit(self, values):
        data = {}
        tax_slip = values[0]
        
        boxes = values[1]
        for line in boxes:
            value = boxes[line][1].get()
            if value == '':
                value = 0
            data[line] = int(value)
        
        self.model.save_tax_slip(data,tax_slip)

        self.view.treeview.insert('', 'end', iid=self.num_slips, text='', values=[tax_slip])
        self.num_slips += 1

        self.switch_view('list')
        

    def calculate_total_income(self):
        return self.model.calculate_total_income()

    def calculate_net_income(self):
        return self.model.calculate_net_income()

    def calculate_taxable_income(self):
        return self.net_income 

    def calculate_federal_tax(self):

        return self.model.calculate_federal_tax()

    def calculate_balance_owing(self):
        return self.model.calculate_refund_balance_owing()

    def calc(self):
        pass

    def open_file(self):
        self.file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))

    
        

    def calculate_return(self):
        
        employment_income, total_income = self.calculate_total_income()
        net_income = self.calculate_net_income()
        basic_personal_amount, total_payable = self.calculate_federal_tax()
        refund_balance = self.calculate_balance_owing()
        
        data = [str(employment_income), '-', str(total_income), str(net_income), str(basic_personal_amount),str(total_payable), '-', str(refund_balance)]

        return data

    def save(self):
        model = m.CSVModel(self.file)
        model.save_record(self.calculate_return())
    
     
# mainloop
if __name__ == '__main__':
    c = Controller()
