import math

type_to_calculate = input("What do you want to calculate?\ntype 'n' for number of monthly payments,\ntype 'a' for annuity monthly payment amount,\ntype 'p' for credit principal:\n")
if type_to_calculate == 'n':
    credit_principal = int(input("Enter the credit principal:\n"))
    monthly_payment_input = int(input("Enter the monthly payment:\n"))
    credit_interest = float(input("Enter the credit interest:\n"))
    i = credit_interest / (12 * 100)
    base = 1 + i
    x = (monthly_payment_input / (monthly_payment_input - i * credit_principal))
    n = math.ceil(math.log(x, base))
    years = int(n / 12)
    months = n - (years * 12)
    if n < 12:
        print("It will take {} months to repay this credit!".format(n))
    elif n == 12:
        print("It will take {} year to repay this credit!".format(n))
    elif (n > 12) and (months == 0):
        print("It will take {} years to repay this credit!".format(years))
    else:
        print("It will take {} years and {} months to repay this credit!".format(years, months))
elif type_to_calculate == 'a':
    credit_principal = int(input("Enter the credit principal:\n"))
    n_of_periods = int(input("Enter the number of periods:\n"))
    credit_interest = float(input("Enter the credit interest:\n"))
    i = credit_interest / (12 * 100)
    a = ((i * ((1 + i) ** n_of_periods)) / (((1 + i) ** n_of_periods) - 1)) * credit_principal
    print("Your monthly payment = {}!".format(math.ceil(a)))
elif type_to_calculate == 'p':
    annuity_payment = float(input("Enter the annuity payment:\n"))
    n_of_periods = int(input("Enter the number of periods:\n"))
    credit_interest = float(input("Enter the credit interest:\n"))
    i = credit_interest / (12 * 100)
    credit_principal = annuity_payment / ((i * ((1 + i) ** n_of_periods)) / (((1 + i) ** n_of_periods) - 1))
    print("Your credit principal = {}!".format(int(credit_principal)))
