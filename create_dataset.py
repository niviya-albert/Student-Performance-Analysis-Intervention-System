import pandas as pd
import random

# First and last names
first_names = [
    "Arjun", "Meera", "Rahul", "Ananya", "Vikram",
    "Sneha", "Kiran", "Divya", "Rohan", "Neha"
]

last_names = [
    "Nair", "Menon", "Das", "Reddy", "Sharma",
    "Iyer", "Kapoor", "Verma", "Pillai", "Joshi",
    "Patel", "Gupta", "Singh", "Kumar", "Shetty",
    "Bose", "Chopra", "Malhotra", "Yadav", "Rao",
    "Kulkarni", "Desai", "Mehta", "Agarwal", "Bhat",
    "Pandey", "Sinha", "Nanda", "Ghosh", "Mishra",
    "Chatterjee", "Saxena", "Tripathi", "Dubey", "Jain",
    "Kohli", "Gill", "Dhawan", "Pandit", "Joshi2",
    "Varma", "Naidu", "Rastogi", "Bhattacharya", "Tiwari",
    "Lal", "Ramesh", "Thomas", "Joseph", "Fernandes"
]

# Shuffle last names for uniqueness
random.shuffle(last_names)

courses = ["DS101", "AI102", "ML201"]

data = []

for i in range(1, 51):
    name = random.choice(first_names) + " " + last_names[i-1]

    student = [
        f"MIT{100+i}",
        name,
        random.choice(courses),
        random.randint(50, 100),
        round(random.uniform(5.0, 9.5), 1),
        random.choice(["Yes", "No"]),
        random.randint(40, 95)
    ]

    data.append(student)

df = pd.DataFrame(data, columns=[
    "student_id",
    "name",
    "course_code",
    "attendance_percent",
    "past_cgpa",
    "test_prep_completed",
    "average_score"
])

df.to_csv("students.csv", index=False)

print("Dataset created successfully with unique names!")