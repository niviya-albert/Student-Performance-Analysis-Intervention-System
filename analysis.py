import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("students.csv")
data["test_prep_completed"] = data["test_prep_completed"].map({"Yes": 1, "No": 0})

def risk_level(row):
    if row["attendance_percent"] < 60 or row["past_cgpa"] < 6:
        return "High Risk"
    elif row["average_score"] < 65:
        return "Medium Risk"
    else:
        return "Low Risk"

data["risk_level"] = data.apply(risk_level, axis=1)

def recommendation(row):
    if row["risk_level"] == "High Risk":
        return "Improve attendance and study consistency"
    elif row["risk_level"] == "Medium Risk":
        return "Focus more on test preparation"
    else:
        return "Maintain performance"

data["suggestion"] = data.apply(recommendation, axis=1)

class_avg = data["average_score"].mean()

course_avg = data.groupby("course_code")["average_score"].mean()

best_course = course_avg.idxmax()
worst_course = course_avg.idxmin()

print("\n===== STUDENT PERFORMANCE REPORT =====")

for index, row in data.iterrows():
    print("\n----- STUDENT REPORT -----")
    print(f"ID: {row['student_id']}")
    print(f"Name: {row['name']}")
    print(f"Course: {row['course_code']}")
    print(f"Attendance: {row['attendance_percent']}%")
    print(f"Past CGPA: {row['past_cgpa']}")
    print(f"Score: {row['average_score']}")
    print(f"Risk Level: {row['risk_level']}")
    print(f"Suggestion: {row['suggestion']}")

print("\n===== CLASS INSIGHTS =====")
print("Class Average Score:", round(class_avg, 2))

if class_avg < 60:
    print("Insight: Overall class performance is low.")

print("\n===== COURSE ANALYSIS =====")
print(course_avg.to_string())

print("\nBest Performing Course:", best_course)
print("Lowest Performing Course:", worst_course)

print(f"\nInsight: {worst_course} shows lower performance and may need improvement.")

plt.figure(figsize=(10,5))

plt.bar(data["name"], data["average_score"])
plt.axhline(y=class_avg,linestyle='--')
plt.xticks(rotation=45)

plt.xlabel("Students")
plt.ylabel("Average Score")
plt.title("Student Performance with Class Average")

plt.tight_layout()

plt.show()

course_avg.plot(kind="bar")
plt.xlabel("Course")
plt.ylabel("Average Score")
plt.title("Course-wise Performance Analysis")
plt.show()