#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

initial_bill = float(input("What was the total bill? $"))
tip_percent = float(
    input("How much tip would you like to give? 10, 12 or 15? ")) / 100
people_number = int(input("How many people to split the bill? "))

total_per_person = initial_bill * (1 + tip_percent) / people_number

rounded_total = round(total_per_person, 2)

print(f"Each person should pay: ${format(rounded_total, '.2f')}")
