# Divisible by 4 → leap year
# BUT if divisible by 100 → NOT a leap year
# UNLESS also divisible by 400 → leap year

year = int(input("Enter a year: "))

def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

print(is_leap_year(year))