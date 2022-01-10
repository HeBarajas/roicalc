class rental_roi:
    def __init__(self, tincome = 0, texpense = 0, ta_cashflow = 0, tccr = 0):
        self.tincome = tincome
        self.texpense = texpense
        self.ta_cashflow = ta_cashflow
        self.tccr = tccr

    def income(self):
        rental = int(input("what is your Rental Income? "))
        laundry = int(input("what is your Laundry Income? "))
        storage = int(input("what is your Storage Income? "))
        misc_in = int(input("what is your Misc Income? "))
        self.tincome = rental + laundry + storage + misc_in
        print("-"*50)
        print(f" Your total monthly income is {self.tincome}")
        print("-"*50)

    def m_expense(self):
        taxes = int(input("what is your monthly taxes expenses? "))
        insurance = int(input("what is your monthly insurance expense? "))
        water_sewer = int(input("what is your monthly water expense? "))
        garbage = int(input("what is your monthly garbage expense? "))
        electric = int(input("what is your monthly electric expense? "))
        gas = int(input("what is your monthly gas expense? "))
        hoa = int(input("what is your monthly hoa expense? "))
        lawn_snow = int(input("what is your monthly lawn and snow care expense? "))
        vacancy = int(input("what is your monthly vacancy expense?"))
        repairs = int(input("what is your monthly repairs expense?"))
        capex = int(input("what is your monthly capex expense? "))
        property_management = int(input("what is your monthly property management expense? "))
        mortage = int(input("what is your monthly mortage expense? "))
        self.texpense = taxes + insurance + water_sewer + garbage + electric + gas + hoa + lawn_snow + vacancy + repairs + capex + property_management + mortage
        print(f"Your total monthly expenses is {self.texpense} ")
    def a_cashflow(self):
        self.ta_cashflow = (self.tincome*12) - (self.texpense*12)
        print("-"*50)
        print(f"your total yearly cashflow is {self.ta_cashflow}")
        print("-"*50)

    def ccr(self):
        downpayment = int(input("what is your total downpayment? "))
        closing_cost = int(input("what is the total closing cost? "))
        rehab_budget = int(input("what is your rehab budget? "))
        misc_ccr = int(input("Any Misc. cost? "))
        investment = downpayment + closing_cost + rehab_budget + misc_ccr
        self.tccr = (self.ta_cashflow / investment)*100
        print("-"*50)
        print(f"Your Cash on Cash ROI is {self.tccr:.2f}%")
        print("-"*50)

def roi():
    roi = rental_roi()
    roi.income()
    roi.m_expense()
    roi.a_cashflow()
    roi.ccr()
roi()