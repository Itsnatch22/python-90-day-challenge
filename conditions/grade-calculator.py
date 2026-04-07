name = input("Enter your name: \n")

subject_1 = int(input("Enter marks for subject 1: \n"))
subject_2 = int(input("Enter marks for subject 2: \n"))
subject_3 = int(input("Enter marks for subject 3: \n"))
subject_4 = int(input("Enter marks for subject 4: \n"))
subject_5 = int(input("Enter marks for subject 5: \n"))

total_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5

average_marks = total_marks / 5

if 90 <= average_marks <= 100:
    print("A")
elif 80 <= average_marks < 90:
    print("B")
elif 70 <= average_marks < 80:
    print("C")
elif 60 <= average_marks < 70:
    print("D")
else:
    print("F")
