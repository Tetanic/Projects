print("Welcome to Clifford\'s Tip Calculator!")
total_bill = input("How much was the total price? $")
total_bill_float = float(total_bill)
party_size = input("How many people participated? ")
tip_amount = input("What percentage would you like to tip?" )
tip_amount_int = int(tip_amount)
party_size_int = int(party_size)
total_with_tip = (total_bill_float / party_size_int) * 1 + tip_amount_int / 100
total_bill_split = (round(total_with_tip, 2))
print(f"Your total bill, if split between {party_size_int} people would be ${total_bill_split}")