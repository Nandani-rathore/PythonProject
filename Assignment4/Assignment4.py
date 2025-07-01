# --------- question1 ---------------

import pandas as pd
data = {
    'name':['payal','Mahima','Diya','Harish','Mayank'],
    'address':['dabi','bundi','bihar','agra','punjab'],
    'ph_no':[1122334455,1234567890,9876543210,6677889900,5544332211],
    'email':['payal@gmail.com','mahima@gmail.com','diya@gmail.com','harish@gmail.com','mayank@gmail.com']

}
df = pd.DataFrame(data)
df.to_csv("Address_book.csv",index=False)
print("\nThe CSV file is :\n")
print(df)
print("CSV file is created Successfully.")




# ----------------------- question2 -------------------------

import pandas as pd

# Create dummy weather data
data = {
    'Date': ['2025-07-01', '2025-07-02', '2025-07-03'],
    'Temperature (C)': [30, 32, 29],
    'Humidity (%)': [70, 65, 80],
    'Condition': ['Sunny', 'Cloudy', 'Rainy']
}

# Convert to DataFrame
weather_df = pd.DataFrame(data)

# Save to CSV
weather_df.to_csv('weather_data.csv', index=False)

# Read the CSV
df = pd.read_csv('weather_data.csv')

# Display data
print("Weather Data:\n", df)

# some more operations
print("\nAverage Temperature:", df['Temperature (C)'].mean())
print("Max Temperature:", df['Temperature (C)'].max())
print("Min Temperature:", df['Temperature (C)'].min())
print("\nDays with Humidity > 70%:\n", df[df['Humidity (%)'] > 70])


# ----------------------- question3 --------------------------

import sqlite3
conn = sqlite3.connect('../college.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
student_id INTEGER PRIMARY KEY AUTOINCREMENT,
name varchar(255),
age INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses(
course_id INTEGER PRIMARY KEY AUTOINCREMENT,
course_name varchar(255),
credits INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS enrollments(
enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
S_ID INTEGER,
course_id INTEGER,
FOREIGN KEY(S_ID) REFERENCES students(student_id),
FOREIGN KEY(course_id) REFERENCES courses(course_id)
)
''')

conn.commit()

# insert records

cursor.executemany("INSERT INTO students(name,age) VALUES (?,?)",[
    ('Nandini',18),
    ('payal',16)
])

cursor.executemany("INSERT INTO courses (course_name,credits) VALUES (?,?)",[
     ("PYTHON",4),
     ("science",2)
])

cursor.executemany("INSERT OR IGNORE INTO enrollments VALUES (?,?,?)",[
    (1,1,101),
    (2,2,102)
])

conn.commit()
print("student table is :\n")
for x in cursor.execute("SELECT * FROM students"):
    print(x)

print("course table is :\n")
for x in cursor.execute("SELECT * FROM courses"):
    print(x)

# update email
cursor.execute("UPDATE Students SET age = 23 WHERE name = 'payal'")
conn.commit()

# 6. Delete some data
cursor.execute("DELETE FROM Courses WHERE course_name = 'Python'")
conn.commit()

# Final display after update and delete
print("\nUpdated Students Table:")
for row in cursor.execute("SELECT * FROM Students"):
    print(row)

print("\nUpdated Courses Table:")
for row in cursor.execute("SELECT * FROM Courses"):
    print(row)

# Close the connection
conn.close()















































