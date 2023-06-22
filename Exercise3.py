#Chea Kimleang 60-19-05-79
loan_amount = int(input("Please amount of loan that you borrow : "))
i = float(input('The interest rate (per year) of the bank : '))
n = int(input("How many year to pay the loan : "))
i = i/12
n = n*12
total_payment = loan_amount*((i*(1+i)**n) / ((1+i)**n-1))
print('The amount to pay every month is : ', total_payment)