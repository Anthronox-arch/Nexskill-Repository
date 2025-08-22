# To calculate percentage of correct answers.

questions = int(input("Enter number of total questions: "))
answers = int(input("Enter number of (correct) answers: "))

print(f"{(answers//questions) * 100}% of answers are correct.")