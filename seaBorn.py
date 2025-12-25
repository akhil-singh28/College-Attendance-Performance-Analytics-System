# College Attendance & Performance Analytics System
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


# STEP 1: Load CSV Files

students = pd.read_csv("DATA/students.csv")
attendance = pd.read_csv("DATA/attendance.csv")
marks = pd.read_csv("DATA/marks.csv")

print("STUDENTS DATA")
print(students.head())

print("\nATTENDANCE DATA")
print(attendance.head())

print("\nMARKS DATA")
print(marks.head())


# STEP 2: Calculate Attendance Percentage

attendance['attendance_percent'] = (
    attendance['attended_classes'] / attendance['total_classes']
) * 100

defaulters = attendance[attendance['attendance_percent'] < 75]

print("\nTop 10 Defaulters (Attendance < 75%)")
print(defaulters.head(10))


# STEP 3: Marks Analysis

weak_students = marks[marks['marks'] < 40]
top_students = marks[marks['marks'] >= 75]

print("\nTop 10 Weak Students (Marks < 40)")
print(weak_students.head(10))

print("\nTop 10 Top Performers (Marks >= 75)")
print(top_students.head(10))


# STEP 4: Attendance vs Marks Analysis

attendance_marks = pd.merge(
    attendance,
    marks,
    on=['student_id', 'subject']
)

student_analysis = attendance_marks.groupby('student_id').agg(
    avg_attendance=('attendance_percent', 'mean'),
    avg_marks=('marks', 'mean')
).reset_index()

print("\nStudent-wise Attendance vs Marks")
print(student_analysis.head())


# STEP 5: DATA VISUALIZATION (FANCY SEABORN GRAPHS)

# 1. Attendance vs Marks (Scatter Plot)
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x='avg_attendance',
    y='avg_marks',
    data=student_analysis,
    hue='avg_marks',
    size='avg_marks',
    palette='viridis',
    sizes=(20, 200),
    alpha=0.8
)
plt.xlabel("Average Attendance (%)")
plt.ylabel("Average Marks")
plt.title("Attendance vs Performance")
plt.show()

# 2️. Subject-wise Marks Distribution
plt.figure(figsize=(8, 5))
sns.barplot(
    x='subject',
    y='marks',
    data=marks,
    palette='coolwarm'
)
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Subject-wise Marks Distribution")
plt.show()

# 3️. Attendance Percentage Distribution
plt.figure(figsize=(8, 5))
sns.histplot(
    attendance['attendance_percent'],
    bins=10,
    kde=True,
    color='skyblue'
)
plt.xlabel("Attendance Percentage")
plt.title("Attendance Percentage Distribution")
plt.show()

print("\n✅ Project Executed Successfully")
