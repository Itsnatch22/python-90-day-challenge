print("Let's check your BMI, shall we!\n")

name = input("Enter your name: \n")

# constant units
KILOGRAMS = "kg"
METERS = "m"

weight = float(input(f"Enter your weight in kilograms ({KILOGRAMS}): "))
height = float(input(f"Enter your height in meters ({METERS}): "))

BMI_findings = weight / (height ** 2)

if BMI_findings >= 30:
    print(f"{name}, you are obese! 😭 Try the gym!")
elif BMI_findings >= 25:
    print(f"{name}, you are overweight! 😂 Try eating healthy!")
elif BMI_findings >= 18.5:
    print(f"{name}, you are normal! 😊 Keep it up!")
else:
    print(f"{name}, you are underweight! 🥲 Eat more!")