def amortization (loan_amount,i,n):
    payment = loan_amount*((i*(1+i)**n) / (((1+i)**n) - 1 ))
    return payment
    
def amortization_table(loan_amount, yearly_interest_rate, number_of_year):
    monthly_interest_rate = yearly_interest_rate / 12
    number_of_month = number_of_year * 12
    principle_balance = loan_amount
    monthly_payment = amortization(loan_amount,monthly_interest_rate,number_of_month)

    print('No,', '|', 'Payment Due','|', 'Interest Due','Principle Due','|','Principle Balance')
    print("------------------------------------------------------")

    i = 1
    while i <= number_of_month:
        interest_due = principle_balance * monthly_interest_rate
        interest_due = round(interest_due,2)
        
        principle_due = monthly_payment - interest_due
        principle_due = round(principle_due,2)

        principle_balance = principle_balance - principle_due
        principle_balance = round(principle_balance,2)

        print(i,'|', monthly_payment, '|', interest_due,'|', principle_due,'|',principle_balance)

        i = i + 1
amortization_table(30000, 0.03, 4)