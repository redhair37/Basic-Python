#If the bill was $150.00, split between 5 people, with 12% tip. 


#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator!")
bill = float(input("What is the bill? "))
percentage = int(input("What percentage tip do you want to give? 10, 12, 15? "))
number = int(input("How many people ate the food? "))
total_percentage = (100 + percentage)/100 
each_person = bill / number
amount_to_pay = round((total_percentage * each_person), 2)

print(f"Amount to be paid by each person ${amount_to_pay}")

