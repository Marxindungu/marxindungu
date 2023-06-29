
weight = input("Enter weight in kilograms")
height = input("Enter height in metres")

weight = float(weight)
height = float(height)

result = weight/(height**2)
print("Your BMI IS", result)

if result < 18.0:
   print("underweight")
elif result <= 18.1:
    print("Normal weight")
elif result <= 29:
    print("Normal weight")
elif result <= 29.1:
    print("Over weight")
elif result <= 34:
    print("Over weight")
elif result > 34.1:
    print("Obese")
