name = input("what is your name? ")
age = int(input("How old are you? "))
city = input("Which city do you live in? ")
print(f"Hi {name} from {city}! In 5 years you will be {age + 5}.")
bill = float(input("How much soes the bill coast? "))
tip_percent = 12
people = 3
tip = bill * tip_percent / 100
total = bill + tip
print(f"Tip: {tip}")
print(f"Total: {total}")
print(f"Each of {people} people pays: {round(total / people, 2)}")
product = "laptop"
price = 500

