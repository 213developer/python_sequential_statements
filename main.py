salary = 0
numDependents = 0
stateTax = 0
federalTax = 0
dependentDeduction = 0
totalWithholding = 0
takeHomePay = 0

# input
salary = float(input("enter your salary"))
numDependents = float(input("enter your number of dependents"))


# Calculate stateTax here.
stateTax = salary * .065

print("State Tax: $" + str(stateTax))

# Calculate federalTax here.
federalTax = salary * .28
print("Federal Tax: $" + str(federalTax))

# Calculate dependantDeduction here.

dependentDeduction = (salary * .025) * numDependents
print("Dependents: $" + str(dependentDeduction))

# Calculate totalWithholding here.
totalWithholding = stateTax + federalTax + dependentDeduction


# Calculate takeHomePay here.
takeHomePay = salary - totalWithholding

print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
