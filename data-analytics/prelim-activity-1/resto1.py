import pandas as pd
import matplotlib.pyplot as plt

# Load the new CSV file
file_path = "data/resto1.csv"  
df = pd.read_csv(file_path)

# Trim column names
df.columns = df.columns.str.strip()

# Find the Item with the Highest Count
highest_count_item = df.loc[df['Count'].idxmax()]

# Find the Item with the Lowest Count
lowest_count_item = df.loc[df['Count'].idxmin()]

# Create a new DataFrame with the required information
summary_data = {
    "Item With Highest Count": [highest_count_item["Item"], highest_count_item["Count"]],
    "Item With Lowest Count": [lowest_count_item["Item"], lowest_count_item["Count"]]
}

# Create a DataFrame from the summary data
summary_df = pd.DataFrame(summary_data, index=["Item ID", "Item Count"])

# Group by color and sum the counts
color_count = df.groupby("Color")["Count"].sum().reset_index()

# Plotting the bar plot
plt.figure(figsize=(8, 6))
plt.bar(color_count["Color"], color_count["Count"], color='lightgreen')

# Add labels and title
plt.xlabel('Color')
plt.ylabel('Total Item Count')
plt.title('Total Item Count per Color')

# Display the plot
plt.show()