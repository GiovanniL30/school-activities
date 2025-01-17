import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file 
file_path = "data/CLASS.csv" 
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

quiz1_total = 50
quiz2_total = 25
exam_total = 100

# Get total quiz score
total_quiz_score = quiz1_total + quiz2_total

# Calculate
df["quiz (50%)"] = ((df["quiz 1"] + df["quiz 2"]) / total_quiz_score * 50 + 50) * 0.5
df["exam (50%)"] = ((df["EXAM"] / exam_total) *  50 + 50) *.50

# Calculate final grade
df["Grade"] = df["quiz (50%)"] + df["exam (50%)"]

# Format numbers
df["quiz (50%)"] = df["quiz (50%)"].round(8)
df["exam (50%)"] = df["exam (50%)"].round(2)
df["Grade"] = df["Grade"].round(2)

# Count total, passing, and failing students
total_students = len(df)
passing_students = (df["Grade"] >= 75).sum()
failing_students = (df["Grade"] < 75).sum()

# Create new summary DataFrame
summary_df = pd.DataFrame({
    "Total Students": [total_students],
    "Passing Students": [passing_students],
    "Failing Students": [failing_students]
})

labels = ['Passing Students', 'Failing Students']
sizes = [passing_students, failing_students]
colors = ['#66b3ff', '#ff6666']  # Colors for pass and fail sections
explode = (0.1, 0)  # Explode the "Passing Students" slice for emphasis

# Plotting the pie chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})
plt.title('Student Performance Distribution')
plt.axis('equal')

# Display the pie chart
plt.show()