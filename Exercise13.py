#Chea Kimleang 60-19-05-79

BASE_HOUR = 40
OT_MULTIPLIER = 2
hours = float(input('Enter the number of hours worked : '))
pay_rate = float(input('Enter the hourly pay rate: '))

if hours > BASE_HOUR:
    overtime_hours = hours - BASE_HOUR
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER
    gross_pay = BASE_HOUR * pay_rate + overtime_pay
else:
    gross_pay = hours * pay_rate
print('The gross pay is : ', gross_pay)