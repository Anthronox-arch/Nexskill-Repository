# To calculate sum of first 'n' natural numbers, where 'n' is the input guven by user.

upperLimit  = int(input("Enter the number to sum upto: "))

i = 1
sum = 0

while i <= upperLimit:
    sum += i
    i += 1

print(f"Sum upto {upperLimit} natural numbers is {sum}.")
