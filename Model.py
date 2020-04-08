import csv

class CSVModel():

    def __init__(self):
         self.tax_slips = {'T3':{}, 'T4':{}, 'T4A':{}, 'T4E':{}, 'T5':{}, 'T2202':{}}
        
    def save_tax_slip(self, data, tax_slip):
        self.tax_slips[tax_slip] = data

    def calculate_total_income(self):
        self.line_10100 =  self.tax_slips['T4'][14]
        self.line_11300 = self.tax_slips['T4A'][18]
        self.line_11400 = self.tax_slips['T4A'][20]
        self.line_11410 = self.tax_slips['T4A'][16]
        self.line_11900 = self.tax_slips['T4E'][14]
        

        self.line_15000 = self.line_10100 + self.line_11300 + self.line_11400 + self.line_11410 + self.line_11900

        total_income = self.line_15000
        employment_income = self.line_10100

        return (employment_income, total_income)

    def calculate_net_income(self,total_income):
        self.line_44 = self.tax_slips['T4'][44]
        self.line_23600 = self.line_15000+ self.line_44
        self.line_26000 = self.line_23600

        net_income = self.line_23600
        return net_income

    def calculate_federal_tax(self):
        #Part A
        self.line_30000 = 12069
        self.line_31200 = self.tax_slips['T4'][18] + self.tax_slips['T4'][55]
        self.line_31260 = min(1222, self.line_10100)
        self.line_25 = 0
        self.line_26 = min(2352, self.line_23600 * 0.03)
        self.line_27= 0 - self.line_26
        self.line_28 = 0
        self.line_29  = self.line_27
        self.line_30 = self.line_30000 + self.line_31200 + self.line_31260 + self.line_29
        self.line_31 = self.line_30 * 0.015
        self.line_32 = self.line_30 * self.line_31
        self.line_34 = self.line_32
        self.line_35000 = self.line_34

        self.line_35 = self.line_26000
        self.line_36 = self.line_35
        
        #Part B
        
        if self.line_35 <= 47630:
            self.line_37 = 0
            self.line_38 = self.line_36 - self.line_37
            self.line_39 = 0.15 * self.line_38
            self.line_40 = self.line_38 * self.line_39
            self.line_41 = 0

        elif 47630 < self.line_35 <= 95259:
            self.line_37 = 47630
            self.line_38 = self.line_36 - self.line_37
            self.line_39 = 0.205
            self.line_40 = self.line_38 * self.line_39
            self.line_41 = 7145

        elif 95259 < self.line_35 <= 147667:
            self.line_37 = 95259
            self.line_38 = self.line_36 - self.line_37
            self.line_39 = 0.26
            self.line_40 = self.line_38 * self.line_39
            self.line_41 = 16908

        elif 147667 < self.line_35 <= 210371:
            self.line_37 = 147667
            self.line_38 = self.line_36 - self.line_37
            self.line_39 = 0.29
            self.line_40 = self.line_38 * self.line_39
            self.line_41 = 30535

        else:
            self.line_37 = 210371
            self.line_38 = self.line_36 - self.line_37
            self.line_39 = 0.33
            self.line_40 = self.line_38 * self.line_39
            self.line_41 = 48719


        self.line_42 = self.line_40 + self.line_41

        #Part C
        self.line_43 = self.line_42
        self.line_44 = 0
        self.line_45 = self.line_43
        self.line_46 = self.line_34
        self.line_47 = 0
        self.line_48 = 0
        self.line_49 = self.line_46
        self.line_50 = self.line_45 - self.line_49
        
        if self.line_50 < 0:
            self.line_50 = 0
            
        self.line_51 = 0
        self.line_52 = self.line_50
        self.line_58 = self.line_50
        self.line_61 = self.line_58

        net_federal_tax = self.line_61
        basic_person_amount = self.line_30000
        total_payable = self.line_35000
        
        
        return basic_person_amount, total_payable

    def calculate_refund_balance_owing(self):
        self.line_42000 = self.line_61
        self.line_43500 = self.line_42000
        
        total_payable = self.line_43500
        self.line_48200 = 0
        
        refund_balance = self.line_43500

        if self.line_43500 < 0:
            self.line_48400 = self.line_43500
        else:
            self.line_48500 = self.line_43500

        return refund_balance
            
            
        
    
        
        
        
        
                
        
