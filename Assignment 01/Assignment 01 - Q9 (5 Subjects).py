# To calculate result of 5 subjects.

firstSubject = int(input("Enter marks of first subject (Out of 20): "))
secondSubject = int(input("Enter marks of second subject (Out of 20): "))
thirdubject = int(input("Enter marks of third subject (Out of 20): "))
fourthSubject = int(input("Enter marks of fourth subject (Out of 20): "))
fifthSubject = int(input("Enter marks of fifth subject (Out of 20): "))

totalMarks = firstSubject + secondSubject + thirdubject + fourthSubject + fifthSubject

print(f"Total marks are {totalMarks}.")
print(f"Percentage is {(totalMarks / 100) * 100}")
print(f"Average is {(totalMarks) / 5}.")


