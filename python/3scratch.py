


def calculate_finances(monthly_income: float, tax_rate: float, montly_expenses: float, currency: str) -> None:
    monthly_tax = monthly_income * (tax_rate / 100)
    monthly_net_income = monthly_income - monthly_tax - montly_expenses
    yearly_salary: float = monthly_income * 12
    yearly_tax = monthly_tax * 12
    yearly_expenses = montly_expenses * 12
    yearly_net_income = yearly_salary - yearly_tax - yearly_expenses

    print('-------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print('-----------------')



def main() -> None:
    while True:
        try:
            monthly_income =  float(input('Enter your monthly salary: '))
            tax_rate =  float(input('Enter your tax rate: (%)')) 
            monthly_expenses =  float(input('Enter your monthly expenses: '))
            break
        except ValueError:
            print('invalid input, try numbers')
        

    calculate_finances(monthly_income, tax_rate, monthly_expenses, currency='EU')
        

if __name__ == '__main__':
    main()


# make a car fuel consumption prog
# or bodu fat, calories
# with classes to put different cars
# 