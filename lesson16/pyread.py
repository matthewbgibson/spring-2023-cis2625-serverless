points = float(input("Enter your score: "))

if points >= 90:
    grade = "A"
    
elif points >= 80:
    grade = "B"
    
elif points >= 70:
    grade = "C"
    
elif points >= 60:
    grade = "D"
    
else:
    grade = "F"

print("Your grade is:", grade)
