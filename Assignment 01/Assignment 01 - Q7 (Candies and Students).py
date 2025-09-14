# To calulate how many candies will be distributed, and how many will be left.

candies = int(input("Enter amount of candies: "))
students = int(input("Enter amount of students: "))

print(f"Each student will get {candies // students} candies.")
print(f"{candies % students} candies will be remaining.")