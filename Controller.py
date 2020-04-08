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
        

    def calculate_total_income(self):
      #  self.employment_income, self.total_income = self.model.calculate_total_income()
        return self.model.calculate_total_income()

    def calculate_net_income(self):
        #self.net_income = self.model.calculate_net_income(self.total_income)
        return self.model.calculate_net_income(self.total_income)

    def calculate_taxable_income(self):
        return self.net_income 

    def calculate_federal_tax(self):
       # self.basic_personal_amount, self.total_payable, self.net_federal_tax = self.model.calculate_federal_tax()
        return self.model.calculate_federal_tax()

    def calculate_balance_owing(self):
       # self.refund_balance = self.model.calculate_refund_balance_owing()
        return self.model.calculate_refund_balance_owing()

    def calculate_return(self):
        
        employment_income, total_income = self.calculate_total_income()
        net_income = self.calculate_net_income()
        basic_personal_amount, total_payable = self.calculate_federal_tax()
        refund_balance = self.calculate_balance_owing()
        if refund_balance < 0:
            value = 'Refund'
        else:
            value = 'Balance Credit' 
        
        
        data = {'Employment Income' : employment_income, 'Employment Insurance': '-', 'Total Income': total_income,
         'Net Income': net_income, 'Basic Personal Amount': basic_personal_amount, 'Total Payable': total_payable,
         'Total Refundable Credits': '-', value: refund_balance}

        return data
        
        
        
        
        
        
    
        


# mainloop
if __name__ == '__main__':
    c = Controller()
