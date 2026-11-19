grade = int(input("Enter the score to know your grade! "))
if grade < 0 or grade > 100:
    letter = "Invalid"
elif grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
   letter = "D"
else:
    letter = "F"
print(f"Score {grade} gives grade {letter}")