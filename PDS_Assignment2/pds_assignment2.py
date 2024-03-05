# -*- coding: utf-8 -*-
"""PDS_Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dglqcV0j1Yr1XmBDnkJDJOe49pJNYr2o

# Loading the Dataset
"""

import pandas as pd

# Load the dataset
data = pd.read_csv('/content/train (1).csv')

print(data)

"""# Check Mising values in the given dataset"""

# Check for missing values in the given dataset
missing_values = data.isnull().sum()
print("Missing values in each column:")
print(missing_values)

"""# a) Look for the missing values in all the columns and either impute them (replace with mean,median, or mode) or drop them. Justify your action for this task."""

# Impute missing values with mode
data['Mileage'].fillna(data['Mileage'].mode()[0], inplace=True)
data['Engine'].fillna(data['Engine'].mode()[0], inplace=True)
data['Power'].fillna(data['Power'].mode()[0], inplace=True)
data['Seats'].fillna(data['Seats'].mode()[0], inplace=True)
data['New_Price'].fillna(data['New_Price'].mode()[0], inplace=True)

# We should avoid dropping the 'New_Price' column since it contains a significant amount of missing data. Removing this column could introduce predictive modeling challenges and bias the results, given its potential importance in understanding the pricing dynamics of used cars.
# So we can take any other column except new_price, here i'm taking price. Still it will not make any significant difference because as we can see there are 0 rows with null value
data.dropna(subset=['Price'], inplace=True)

# Check if missing values are handled
print("After handling missing values:")
print(data.isnull().sum())

# Save the output dataset
data.to_csv('afterHandlingMissingValues.csv', index=False)

"""# b) Remove the units from some of the attributes and only keep the numerical values (for example remove kmpl from “Mileage”, CC from “Engine”, bhp from “Power”, and lakh from “New_price”)."""

# Remove units from attributes
# We use the str.extract() method along with regular expressions to extract numerical values from the specified attributes while removing the units.
data['Mileage'] = data['Mileage'].str.extract('(\d+.\d+)', expand=False)
data['Engine'] = data['Engine'].str.extract('(\d+)', expand=False)
data['Power'] = data['Power'].str.extract('(\d+.\d+)', expand=False)
data['New_Price'] = data['New_Price'].str.extract('(\d+.\d+)', expand=False)

# Convert data types to numeric
# After extraction, converting attributes to numeric types using `pd.to_numeric()` ensures only numerical values persist, facilitating subsequent analysis or processing.
data['Mileage'] = pd.to_numeric(data['Mileage'], errors='coerce')
data['Engine'] = pd.to_numeric(data['Engine'], errors='coerce')
data['Power'] = pd.to_numeric(data['Power'], errors='coerce')
data['New_Price'] = pd.to_numeric(data['New_Price'], errors='coerce')

# Display the modified dataset
print(data.head())

# Save the output dataset
data.to_csv('removingTheUnits.csv', index=False)

"""# c) Change the categorical variables (“Fuel_Type” and “Transmission”) into numerical one hot encoded value."""

# Convert categorical variables into one-hot encoded values
# To convert categorical variables into numerical one-hot encoded values, we can use the pd.get_dummies() function in pandas
data = pd.get_dummies(data, columns=['Fuel_Type', 'Transmission'])

print(data.head())

# Save the output dataset
data.to_csv('hotEncodedValue.csv', index=False)

"""# d) Create one more feature and add this column to the dataset (you can use mutate function in R for this). For example, you can calculate the current age of the car by subtracting “Year” value from the current year."""

import pandas as pd
from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Calculate the current age of the car
data['Current_Age'] = current_year - data['Year']

print(data.head())

# Save the output dataset
data.to_csv('addAColumnToTheDataset.csv', index=False)

"""# e) Perform select, filter, rename, mutate, arrange and summarize with group by operations (or their equivalent operations in python) on this dataset."""

# Select operation: Select specific columns
selected_data = data[['Name', 'Location', 'Year', 'Kilometers_Driven', 'Fuel_Type_Diesel', 'Fuel_Type_Electric', 'Fuel_Type_Petrol', 'Price']]

# Filter operation: Filter rows based on a condition
# Example filter condition: cars with price greater than 10 lakhs
filtered_data = data[data['Price'] > 10]

# Rename operation: Rename columns
renamed_data = data.rename(columns={'Kilometers_Driven': 'Kms_Driven'})

# Mutate operation: Create a new column based on existing columns
data['Mileage_per_Km'] = data['Mileage'] / data['Kilometers_Driven']

# Arrange operation: Sort the dataset based on a column
sorted_data = data.sort_values(by='Year', ascending=False)

# Summarize operation: Calculate summary statistics
summary_stats = data.describe()

# Group by operation: Group data based on a categorical variable and perform summary statistics
grouped_data = data.groupby('Fuel_Type_Diesel').agg({'Price': 'mean', 'Year': 'min', 'Kilometers_Driven': 'max'})

# Display the results
print("Selected Data:")
print(selected_data.head())

print("\nFiltered Data:")
print(filtered_data.head())

print("\nRenamed Data:")
print(renamed_data.head())

print("\nMutated Data:")
print(data.head())

print("\nSorted Data:")
print(sorted_data.head())

print("\nSummary Statistics:")
print(summary_stats)

print("\nGrouped Data:")
print(grouped_data)

# Save the output dataset
data.to_csv('afterPerformingAllTheOperations.csv', index=False)