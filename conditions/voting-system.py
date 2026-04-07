name = input("Enter your name: ")

current_age = int(input("Enter your age: "))

voting_age = 18

years_until_eligible = voting_age - current_age

if current_age >= 18:
    print(f"Hello, {name}! You can proceed with the voting process. Thank you.")
else:
    print(f"Hello, {name}! You are not eligible to vote yet. You need to wait {years_until_eligible} years.")