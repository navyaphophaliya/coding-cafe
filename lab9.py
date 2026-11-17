import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# PART 1

growth = np.array([4, 7, 5, 9, 6, 8])

average_growth = np.mean(growth)
maximum_growth = np.max(growth)
minimum_growth = np.min(growth)
total_growth = np.sum(growth)

print("Average growth:", average_growth)
print("Maximum growth:", maximum_growth)
print("Minimum growth:", minimum_growth)
print("Total growth:", total_growth)

tall_plants = growth[growth > 5]
print("Plants with growth above 5:", tall_plants)


# Task 1

temperatures = np.array([22, 25, 21, 28, 24])

average_temperature = np.mean(temperatures)
highest_temperature = np.max(temperatures)
lowest_temperature = np.min(temperatures)

above_23 = temperatures[temperatures > 23]
count_above_23 = len(above_23)

print("\nTASK 1: TEMPERATURE MONITORING")
print("Average temperature:", average_temperature)
print("Highest temperature:", highest_temperature)
print("Lowest temperature:", lowest_temperature)
print("Temperatures above 23:", above_23)
print("Number of days above 23:", count_above_23)

# PART 2

data = {
    'Plant': ['Rose', 'Tulip', 'Lily', 'Rose', 'Tulip'],
    'Initial_Height': [10, 12, 8, 11, 14],
    'Final_Height': [18, 20, 15, 17, 23],
    'Sunlight': [6, 7, 5, 8, 6]
}

plants_df = pd.DataFrame(data)

print("\nPLANT DATASET")
print(plants_df.head())

print("Shape:", plants_df.shape)
print("Columns:", plants_df.columns)

print("\nFinal Heights:")
print(plants_df['Final_Height'])

taller_plants = plants_df[plants_df['Final_Height'] > 12]

print("\nPlants with height above 12:")
print(taller_plants)

average_height = plants_df.groupby('Plant')['Final_Height'].mean()

print("\nAverage height of each plant:")
print(average_height)


# Task 2

plants_df['Growth'] = plants_df['Final_Height'] - plants_df['Initial_Height']

print("\nPlant and Growth:")
print(plants_df[['Plant', 'Growth']])

high_growth = plants_df[plants_df['Growth'] > 7]

print("\nPlants that grew more than 7 cm:")
print(high_growth)

average_plant_growth = plants_df.groupby('Plant')['Growth'].mean()

print("\nAverage growth for each plant:")
print(average_plant_growth)

# PART 3: MATPLOTLIB


plants = ['Rose', 'Tulip', 'Lily', 'Sunflower']
heights = [15, 20, 12, 25]

plt.bar(plants, heights)

plt.title("Plant Heights")
plt.xlabel("Plant")
plt.ylabel("Height (cm)")

plt.show()


# Task 3

weeks = [1, 2, 3, 4, 5]
growth = [3, 6, 9, 14, 20]

plt.plot(weeks, growth, marker='o')

plt.title("Plant Growth Over Five Weeks")
plt.xlabel("Week")
plt.ylabel("Growth (cm)")

plt.grid()

plt.show()


# PART 4

student_data = {
    'Student': ['Asha', 'Jess', 'Meera', 'Rohan', 'Sara', 'Dev'],
    'Physics': [85, 72, 95, 65, 88, 78],
    'Chemistry': [78, 88, 91, 70, 84, 76],
    'Biology': [92, 80, 89, 75, 90, 82]
}

students_df = pd.DataFrame(student_data)

print("\nSCHOOL SCIENCE FAIR DATASET")
print(students_df)

physics_scores = np.array(students_df['Physics'])

average_physics = np.mean(physics_scores)
highest_physics = np.max(physics_scores)
lowest_physics = np.min(physics_scores)

print("\nPHYSICS STATISTICS")
print("Average Physics score:", average_physics)
print("Highest Physics score:", highest_physics)
print("Lowest Physics score:", lowest_physics)

students_df['Total'] = (
    students_df['Physics']
    + students_df['Chemistry']
    + students_df['Biology']
)

students_df['Average'] = students_df['Total'] / 3

print("\nStudent totals and averages:")
print(students_df)

high_scorers = students_df[students_df['Average'] > 80]

print("\nStudents with average above 80:")
print(high_scorers)

highest_average = students_df['Average'].max()

top_student = students_df[
    students_df['Average'] == highest_average
]

print("\nHighest average:", highest_average)
print("Top-performing student:")
print(top_student)

plt.bar(students_df['Student'], students_df['Average'])

plt.title("Average Marks of Students")
plt.xlabel("Student")
plt.ylabel("Average Marks")

plt.grid()

plt.show()

print("\nSCIENCE FAIR QUESTIONS")

print(
    "1. Student with highest Physics score:",
    students_df.loc[students_df['Physics'].idxmax(), 'Student']
)

print("2. Average Physics score:", average_physics)

print(
    "3. Student with highest overall average:",
    top_student['Student'].values[0]
)

print("4. Number of students with average above 80:", len(high_scorers))

