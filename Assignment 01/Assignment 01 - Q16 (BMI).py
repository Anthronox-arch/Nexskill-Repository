# To calculate BMI using mass and height.

mass = int(input("Enter mass in kilograms: "))
height = int(input("Enter height in metres: "))

BMI = mass/(height ** 2)

print(f"BMI is {BMI}.")