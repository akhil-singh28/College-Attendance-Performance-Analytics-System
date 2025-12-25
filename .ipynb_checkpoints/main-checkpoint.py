import pandas as pd

# Load CSV files
students = pd.read_csv("DATA/students.csv")
attendance = pd.read_csv("DATA/attendance.csv")
marks = pd.read_csv("DATA/marks.csv")

# Display data
print("STUDENTS DATA")
print(students)

print("\nATTENDANCE DATA")
print(attendance)

print("\nMARKS DATA")
print(marks)
