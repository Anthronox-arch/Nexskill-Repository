# To convert minutes to hour and minutes.

minutes = int(input("Enter number of minutes: "))

if minutes >= 60:
    print(f"{minutes} minutes in hours is {minutes // 60} hours and {minutes % 60} minutes.")
    
else:
    print("Please enter an amount greater than or equal to 60.")