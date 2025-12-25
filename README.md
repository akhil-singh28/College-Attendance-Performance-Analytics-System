<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>📊 College Attendance & Performance Analytics System</h1>

  <h2>📌 Overview</h2>
  <p>
    This project analyzes student attendance and academic performance using Python.<br>
    It identifies defaulters, weak performers, and top scorers, and visualizes trends between attendance and marks.
  </p>

  <h2>🗂️ Project Structure</h2>
  <pre>
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
  </pre>

  <h2>🚀 Features</h2>
  <ul>
    <li>Calculate attendance percentage per student</li>
    <li>Identify:
      <ul>
        <li>🔴 Weak students (Marks &lt; 40)</li>
        <li>🟢 Top performers (Marks ≥ 75)</li>
        <li>⚠️ Defaulters (Attendance &lt; 75%)</li>
      </ul>
    </li>
    <li>Subject-wise marks analysis</li>
    <li>Visualizations:
      <ul>
        <li>Attendance vs Marks (Scatter Plot)</li>
        <li>Subject-wise Marks (Bar Plot)</li>
        <li>Attendance Distribution (Histogram / KDE)</li>
      </ul>
    </li>
  </ul>

  <h2>🛠️ Technologies Used</h2>
  <ul>
    <li>Python</li>
    <li>Pandas, NumPy</li>
    <li>Matplotlib</li>
    <li>Seaborn (optional for enhanced visuals)</li>
  </ul>

  <h2>▶️ How to Run</h2>
  <h3>Step 1: Install dependencies</h3>
  <pre><code>pip install pandas numpy matplotlib seaborn</code></pre>

  <h3>Step 2: Run either version</h3>
  <ul>
    <li>Matplotlib:
      <pre><code>python main.py</code></pre>
    </li>
    <li>Seaborn:
      <pre><code>python seaBorn.py</code></pre>
    </li>
  </ul>

  <h2>📊 Sample Visuals</h2>
  <ul>
    <li>Scatter plot showing correlation between attendance and marks</li>
    <li>Bar chart of subject-wise marks</li>
    <li>Histogram/KDE of attendance distribution</li>
  </ul>

</body>
</html>
