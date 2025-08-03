# Week1- Activity 3: Temperature Analysis Using Python and NumPy
# Develop a Python project to perform the following tasks:
# Calculate and print the average temperature for the week using NumPy.
# Temperature data (in °C): [18.5, 19, 20, 25.0, 2, 30, 13.9]
# Determine and display the highest and lowest recorded temperatures.
# Convert all temperatures to Fahrenheit and print the converted values.
# (Use the formula: F = C × 9/5 + 32)
# Identify and print the indices of days where the temperature exceeded 20°C.
import numpy as np
temp=np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
avg_temp = np.mean(temp)
print(f"Average temperature for the week: {avg_temp:.2f}°C")
# (.2f means showing two decimal number"18.76")

max_value=np.max(temp)
min_value=np.min(temp)  
print(f"Highest number:{max_value}°C")  
print(f"Lowest number: {min_value}°C")

celsius_temp=np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
fahrenheit_temp=celsius_temp*9/5+32
print("Temperature in fahrenheit:",fahrenheit_temp)

hotdays_indices=np.where(celsius_temp>20)
print("Indices of days with temperature more than 20°C:", hotdays_indices[0])
