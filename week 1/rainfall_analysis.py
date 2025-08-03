# week1- activity 4: Rainfall Analysis with NumPy
# Sample rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]


# Tasks: 
# Convert the list to a NumPy array and print it.
# Print the total rainfall for the week.
# Print the average rainfall for the week.
# Count how many days had no rain (0 mm).
# Print the days (by index) where the rainfall was more than 5 mm.
# Share your GitHub link on Teams when you have done.
import numpy as np
rain=np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
my_array = np.array(rain)
print(f"Rainfall list:{my_array} mm")

total=sum(rain)
print(f"Total rainfall for week:{total} mm")

count=len(rain)
average=total/count
print(f"Average rainfall for week:{average} mm")

no_raindays = np.sum(rain == 0.0)
print("Number of days with no rain:", no_raindays)

more_raindays=np.where(rain>5)
print("Days where rainfall was more than 5mm:",more_raindays[0])