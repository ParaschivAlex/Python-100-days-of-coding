print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

tip_percentage = percentage/100
total_tip = bill*tip_percentage
total_bill = bill+total_tip
bill_person = total_bill/people
final_amount = round(bill_person, 2)
final_amount = "{:.2f}".format(bill_person)
print(f"Each person should pay: ${final_amount}")


