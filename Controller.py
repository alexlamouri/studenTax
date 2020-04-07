import tkinter as tk
import tkinter.ttk as ttk
import Model as m
from View import View as v

class Controller():

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("StudenTax")

        # mvc
        self.model = m.CSVModel()
        self.view = v(self.root, self)

        self.root.mainloop()

    def switch_view(self, new_view):

        for old_view in self.view.views:
            self.view.views[old_view].grid_forget()

        self.view.views[new_view].grid(row=0, column=0)

    def submit(self, values):
        data = {}
        tax_slip = values[0]
        # print(tax_slip)
        boxes = values[1]
        for line in boxes:
            value = boxes[line][1].get()
            if value == '':
                value = 0
            data[line] = int(value)
        
        self.model.save_tax_slip(data,tax_slip)
        

    def total_income(self):
        self.total_income = self.model.calculate_total_income()
        return self.total_income

    def net_income(self):
        self.net_income = self.model.calculate_net_income(self.total_income)
        return self.net_income

    def taxable_income(self):
        return self.net_income 

    def federal_tax(self):
        self.net_federal_tax = self.model.calculate_federal_tax()
        return self.net_federal_tax

    def balance_owing(self):
        self.refund_balance = self.model.calculate_refund_balance_owing()
        return self.refund_balance

    def calculate_return(self):
        self.total_income()
        self.net_income()
        self.taxable_income()
        self.federal_tax()
        self.balance_owing()
        print(self.total_income)
        print(self.net_income)
        print(self.net_federal_tax)
        print(self.refund_balance)
        
        
    
        


# mainloop
if __name__ == '__main__':
    c = Controller()
