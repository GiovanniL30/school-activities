import csv_util
import statistics

#Load all csv data
class_data = csv_util.read('data/CLASS.csv')
resto_data = csv_util.read('data/resto1.csv')
sample_data = csv_util.read('data/SAMPLE.csv')

# Calculates the median of a given numeric column.
def calculate_median(data, column_name):
    if column_name not in data["fields"]:
        return f"Column '{column_name}' not found."

    col_index = data["fields"].index(column_name)
    values = []

    for row in data["rows"]:
        column_value = row[col_index]

        if column_value.replace('.', '', 1).isdigit():
            values.append(float(column_value))

    if not values:
        return f"No valid numeric data found in column '{column_name}'."

    return statistics.median(values)

# Calculates the variance of a given numeric column.
def calculate_variance(data, column_name):
 
    if column_name not in data["fields"]:
        return f"Column '{column_name}' not found."

    col_index = data["fields"].index(column_name)
    values = []

    for row in data["rows"]:
        column_value = row[col_index]

        if column_value.replace('.', '', 1).isdigit():
            values.append(float(column_value))

    if not values:
        return f"No valid numeric data found in column '{column_name}'."

    return statistics.variance(values) 

#Calculates the standard deviation of a given numeric column.
def calculate_stddev(data, column_name):
   
    if column_name not in data["fields"]:
        return f"Column '{column_name}' not found."

    col_index = data["fields"].index(column_name)
    values = []

    for row in data["rows"]:
        column_value = row[col_index]

        if column_value.replace('.', '', 1).isdigit():
            values.append(float(column_value))

    if not values:
        return f"No valid numeric data found in column '{column_name}'."

    return statistics.stdev(values)


#calculates average of a given column data
def calculate_average(data, column_name):

    if column_name not in data["fields"]:
        return f"Column '{column_name}' not found."

    column_index = data["fields"].index(column_name)
    values = []

    for row in data["rows"]:
        try:
            values.append(float(row[column_index]))
        except ValueError:
            pass 

    if not values:
        return f"No valid numeric data found in column '{column_name}'."

    return statistics.mean(values)


#gets the mode of a given column data
def get_mode(data, column_name):
    if column_name not in data["fields"]:
        return f"Column '{column_name}' not found."

    column_index = data["fields"].index(column_name)
    values = [row[column_index] for row in data["rows"] if row[column_index]] 

    if not values:
        return f"No valid data found in column '{column_name}'."

    try:
        numeric_values = [float(value) for value in values]
        return statistics.multimode(numeric_values)  
    except ValueError:
        return statistics.multimode(values)  
    
# Calculates the average of a given numeric column for a specific column
def calculate_average_by(data, column_name, filter_value, filter_column ):
   
    if column_name not in data["fields"] or filter_column not in data["fields"]:
        return f"Column '{column_name}' or '{filter_column}' not found."

    col_index = data["fields"].index(column_name)
    filter_index = data["fields"].index(filter_column)
    values = []  

    for row in data["rows"]:
        if row[filter_index] == filter_value:  
            column_value = row[col_index]

            if column_value.replace('.', '', 1).isdigit():  # Checks if it's a valid number
                values.append(float(column_value))

    if not values:
        return f"No valid numeric data found for '{filter_value}' in column '{column_name}'."

    return statistics.mean(values)


