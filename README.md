📊 College Attendance & Performance Analytics System
📌 Overview
This project analyzes student attendance and academic performance using Python.
It identifies defaulters, weak performers, and top scorers, and visualizes trends between attendance and marks.

🗂️ Project Structure
Code
College-Attendance-Performance-Analytics-System/
├── Data/
│   ├── attendance.csv
│   ├── marks.csv
│   └── students.csv
├── main.py                 # Matplotlib version
├── seaBorn.py              # Seaborn version
├── README_matplotlib.md    # Documentation for matplotlib version
├── README_seaborn.md       # Documentation for seaborn version
├── report_matplotlib.docx  # Report for matplotlib version
├── report_seaborn.docx     # Report for seaborn version
🚀 Features
Calculate attendance percentage per student

Identify:

🔴 Weak students (Marks < 40)

🟢 Top performers (Marks ≥ 75)

⚠️ Defaulters (Attendance < 75%)

Subject-wise marks analysis

Visualizations:

Attendance vs Marks (Scatter Plot)

Subject-wise Marks (Bar Plot)

Attendance Distribution (Histogram / KDE)

🛠️ Technologies Used
Python

Pandas, NumPy

Matplotlib

Seaborn (optional for enhanced visuals)

▶️ How to Run
Install dependencies:

Step-1
**pip install pandas numpy matplotlib seaborn**
Step-2
Run either version:

1.Matplotlib:
                **python main.py**
2.Seaborn:
                **python seaBorn.py**
📊 Sample Visuals
Scatter plot showing correlation between attendance and marks

Bar chart of subject-wise marks

Histogram/KDE of attendance distribution
