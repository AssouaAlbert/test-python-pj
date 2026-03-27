import sys
"""
Tip Calculator
A simple command-line application that calculates the tip amount and total bill.
This module handles Python 2/3 compatibility for the input function,
then prompts the user to enter:
- The bill amount
- The tip percentage
It then calculates and displays:
- The tip amount
- The total amount to pay (bill + tip)
Example:
    Enter the bill amount: 50
    Enter the tip percentage (e.g., 15 for 15%): 20
    Tip amount: $10.00
    Total amount to pay: $60.00
"""
if sys.version_info < (3, 0):
    input = raw_input  # For Python 2 compatibility
else:
    print(sys.version_info)

bill = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount to pay: ${total_amount:.2f}")