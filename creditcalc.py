import math
import sys


def time_to_repay(credit_interest, monthly_payment, credit_principal):
    i = credit_interest / (12 * 100)
    base = 1 + i
    x = (monthly_payment / (monthly_payment - i * credit_principal))
    n = math.ceil(math.log(x, base))
    years = int(n / 12)
    the_months = n - (years * 12)
    if n < 12:
        print("It will take {} months to repay this credit!".format(n))
    elif n == 12:
        print("It will take {} year to repay this credit!".format(n))
    elif (n > 12) and (the_months == 0):
        print("It will take {} years to repay this credit!".format(years))
    else:
        print("It will take {} years and {} months to repay this credit!".format(years, the_months))
    overpayment = (monthly_payment * n) - credit_principal
    print("Overpayment = {}".format(int(overpayment)))


def annuity_payment(credit_interest, n_of_periods, credit_principal):
    i = credit_interest / (12 * 100)
    a = math.ceil(((i * ((1 + i) ** n_of_periods)) / (((1 + i) ** n_of_periods) - 1)) * credit_principal)
    print("Your annuity payment = {}!".format(a))
    overpayment = (a * n_of_periods) - credit_principal
    print("Overpayment = {}".format(int(overpayment)))


def calculating_principle(credit_interest, annuity_payment, n_of_periods):
    i = credit_interest / (12 * 100)
    credit_principal = math.floor(annuity_payment / ((i * ((1 + i) ** n_of_periods)) / (((1 + i) ** n_of_periods) - 1)))
    print("Your credit principal = {}!".format(credit_principal))
    overpayment = (annuity_payment * n_of_periods) - credit_principal
    print("Overpayment = {}".format(int(overpayment)))


def differentiated_payment(n_of_periods, credit_principal, credit_interest):
    months = 0
    final_payment = 0
    while months < n_of_periods:
        i = credit_interest / (12 * 100)
        diff_payment = math.ceil((credit_principal / n_of_periods) + (i * (credit_principal - ((credit_principal * months) / n_of_periods))))
        months += 1
        print("Month {}: payment is {}".format(months, diff_payment))
        final_payment += diff_payment
    print("Overpayment = {}".format(int(final_payment - credit_principal)))


def get_arguments():
    inp_principal = 0
    inp_payment = 0
    inp_periods = 0
    inp_interest = 0
    for i in args:
        arg = i.split('=')
        if arg[0] == '--principal':
            inp_principal = int(arg[1])
        if arg[0] == '--payment':
            inp_payment = float(arg[1])
        if arg[0] == '--periods':
            inp_periods = int(arg[1])
        if arg[0] == '--interest':
            inp_interest = float(arg[1])
    return inp_principal, inp_payment, inp_periods, inp_interest


args = sys.argv

if (args[1] != '--type=annuity' or args[1] != '--type=diff') and (len(args) != 5):
    print("Incorrect parameters")
else:
    if args[1] == '--type=annuity':
        arguments = get_arguments()
        principal = arguments[0]
        payment = arguments[1]
        periods = arguments[2]
        interest = arguments[3]
        if interest == 0:
            print("Incorrect parameters")
        if periods < 0:
            print("Incorrect parameters")
        if periods == 0:
            time_to_repay(interest, payment, principal)
        if payment == 0:
            annuity_payment(interest, periods, principal)
        if principal == 0:
            calculating_principle(interest, payment, periods)
    if args[1] == '--type=diff':
        arguments = get_arguments()
        principal = arguments[0]
        payment = arguments[1]
        periods = arguments[2]
        interest = arguments[3]
        if payment != 0 or periods < 0:
            print("Incorrect parameters")
        else:
            differentiated_payment(periods, principal, interest)
