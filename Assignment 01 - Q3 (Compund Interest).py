# To calculate compund interest.

principal = int(input("Enter the principal: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the tiem: "))
compundInterest = (principal * (1 + (rate/100)**time)) - principal

print(f"Compund interest according to given data is {compundInterest}.")