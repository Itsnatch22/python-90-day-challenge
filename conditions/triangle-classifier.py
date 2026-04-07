#rules
# An equilateral triangle (all sides equal)
# An isosceles triangle (two sides equal)
# A scalene triangle (no sides equal)
# Not a valid triangle (triangle inequality theorem)

#input
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

#logic
if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
elif side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("Scalene triangle")
else:
    print("Not a valid triangle")