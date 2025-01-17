import pandas as pd
import matplotlib.pyplot as plt

# Load the new CSV file
file_path = "data/SAMPLE.csv"
df = pd.read_csv(file_path)

# Calculate average age per course
average_age_per_course = df.groupby("COURSE")["AGE"].mean().reset_index()

# Convert the average age to integers (removing decimals)
average_age_per_course["AGE"] = average_age_per_course["AGE"].astype(int)

average_age_per_course.columns = ["Course", "Average Age"]

# Plotting the bar plot
plt.figure(figsize=(8, 6))
plt.bar(average_age_per_course["Course"], average_age_per_course["Average Age"], color='skyblue')

# Add labels and title
plt.xlabel('Course')
plt.ylabel('Average Age')
plt.title('Average Age per Course')

# Display the plot
plt.show()

# Calculate the student count per course
student_count_per_course = df.groupby("COURSE").size().reset_index(name='Student Count')

# Plotting the bar plot for student count per course
plt.figure(figsize=(8, 6))
plt.bar(student_count_per_course["COURSE"], student_count_per_course["Student Count"], color='lightcoral')

# Add labels and title
plt.xlabel('Course')
plt.ylabel('Student Count')
plt.title('Student Count per Course')

# Display the plot
plt.show()