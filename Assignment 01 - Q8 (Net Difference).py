# To calculate profit and losses.

costPrice = int(input("Enter the cost price: "))
sellingPrice = int(input("Enter the selling price: "))

difference = sellingPrice - costPrice

if difference > 0:
    print(f"You have made a profit of {sellingPrice - costPrice}.")
elif difference < 0:
    print(f"You have made a loss of {sellingPrice - costPrice}.")
else:
    print(f"Net difference is 0 i.e., you have made neither a profit nor a loss.")