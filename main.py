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

# Attendance Percentage
# Calculate attendance percentage
attendance['attendance_percent'] = (
    attendance['attended_classes'] / attendance['total_classes']
) * 100

# Find defaulters (attendance < 75%)
defaulters = attendance[attendance['attendance_percent'] < 75]

# Display top 10 defaulters
print("\nTop 10 Students with Low Attendance (<75%)")
print(defaulters.head(10))

# Marks Analysis
# Weak students (marks < 40)
weak_students = marks[marks['marks'] < 40]

print("\nTop 10 Weak Students (Marks < 40)")
print(weak_students.head(10))

# Top students (marks >= 75)
top_students = marks[marks['marks'] >= 75]

print("\nTop 10 Top-Performing Students (Marks >= 75)")
print(top_students.head(10))


#Attendance vs Marks
# Merge attendance and marks data
attendance_marks = pd.merge(
    attendance,
    marks,
    on=['student_id', 'subject']
)

print("\nMerged Attendance + Marks Data")
print(attendance_marks.head(10))

# Average attendance and marks per student
student_analysis = attendance_marks.groupby('student_id').agg(
    avg_attendance=('attendance_percent', 'mean'),
    avg_marks=('marks', 'mean')
).reset_index()

print("\nStudent-wise Attendance vs Marks")
print(student_analysis.head(10))

#DATA VISUALIZATION USING MATPLOTLIB

import matplotlib.pyplot as plt
# Attendance vs Marks
plt.figure()
plt.scatter(student_analysis['avg_attendance'], student_analysis['avg_marks'])
plt.xlabel("Average Attendance (%)")
plt.ylabel("Average Marks")
plt.title("Attendance vs Performance")
plt.show()

# Subject-wise Average Marks
subject_avg_marks = marks.groupby('subject')['marks'].mean()

plt.figure()
subject_avg_marks.plot(kind='bar')
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")
plt.show()

# Attendance Percentage Distribution
plt.figure()
attendance['attendance_percent'].plot(kind='hist', bins=10)
plt.xlabel("Attendance Percentage")
plt.title("Attendance Percentage Distribution")
plt.show()
