# To calculate salary.

basicSalary = int(input("Enter your basic salary: "))

HRA = 0.20 * basicSalary
DA = 0.15 * basicSalary
totalSalary = basicSalary + HRA + DA

print(f"Your total salary is {totalSalary}.")