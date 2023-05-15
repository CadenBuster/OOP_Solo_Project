class ROI():
    def __init__(self):
        self.tmi = 0
        self.tme = 0
        self.expenses = {}
        self.income = {}
        self.cash_flow = 0




    def funct_income(self):
        
        income_src = input("What are you making money on? ")
        income_amount = int(input("How much money per month do you make from this? "))
        self.income[income_src] = income_amount
        self.tmi += self.income[income_src]
        print(self.income)
        print(self.tmi)


    def funct_expenses(self):
        expense_src = input("What is costing you money? ")
        expense_amount = int(input("How much money is this costing per month? "))
        self.expenses[expense_src] = expense_amount
        self.tme += self.expenses[expense_src]
        print(self.expenses)
        print(self.tme)

    def funct_cashflow(self):
        self.cash_flow = self.tmi - self.tme
        print(self.cash_flow)

    def funct_cashon_roi(self):
        
        total_invest = int(input("How much did you invest into it? "))
        acf = self.cash_flow * 12
        cocroi = (acf / total_invest) * 100
        print(f'Your final return on investment for this property is {cocroi}%.')



    def runner(self):
        print("Welcome to the ROI calculator.")
        print("To get started, follow the prompts below: ")
        while True:
            print(" ")
            print("Would you like to access income/expenses/calculate ROI/ or exit the program?")
            user_choice = input("Please select one INCOME/EXPENSES/CALCULATE/QUIT: ")
            if user_choice.lower() == "income":
                self.funct_income()
            elif user_choice.lower() == "expenses":
                self.funct_expenses()
            elif user_choice.lower() == "calculate":
                if self.tmi == 0 or self.tme == 0:
                    print("Looks like theres a few more steps that need to be done before we can calculate your ROI.")
                else: 
                    self.funct_cashflow()
                    self.funct_cashon_roi()
            elif user_choice.lower() == "quit":
                print("Thank you for visiting the ROI Calculator!")
                break
            else:
                print("Invalid response. Please Try again")


calculator = ROI()


print(calculator.runner())

