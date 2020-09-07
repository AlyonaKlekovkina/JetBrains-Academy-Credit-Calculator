# credit_principal = 'Credit principal: 1000'
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'

# print('{}\n{}\n{}\n{}\n{}'.format(credit_principal, first_month, second_month, third_month, final_output))
import math
credit_principal = int(input("Enter the credit principal:\n"))
type_to_calculate = input("What do you want to calculate?\ntype 'm' - for number of monthly payments,\ntype 'p' - for the monthly payment:\n")
if type_to_calculate == 'm':
    monthly_payment_input = int(input("Enter the monthly payment:\n"))
    months_to_pay = math.ceil(credit_principal / monthly_payment_input)
    if months_to_pay == 1:
        print("It will take {} month to repay the credit".format(months_to_pay))
    else:
        print("It will take {} months to repay the credit".format(months_to_pay))
elif type_to_calculate == 'p':
    number_of_month_input = int(input("Enter the number of months:\n"))
    monthly_payment = math.ceil(credit_principal / number_of_month_input)
    last_payment = credit_principal - ((number_of_month_input - 1) * monthly_payment)
    if last_payment == monthly_payment:

        print("Your monthly payment = {}".format(monthly_payment))
    else:
        print("Your monthly payment = {} and the last payment = {}.".format(monthly_payment, last_payment))
