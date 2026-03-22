import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("students.csv")

# Convert test prep to numeric
data["test_prep_completed"] = data["test_prep_completed"].map({"Yes": 1, "No": 0})

# -------------------------------
# PERFORMANCE SCORE
# -------------------------------
data["performance_score"] = (
    data["attendance_percent"] * 0.3 +
    data["past_cgpa"] * 10 * 0.2 +
    data["test_prep_completed"] * 10 * 0.1 +
    data["average_score"] * 0.4
)

# -------------------------------
# RISK CLASSIFICATION (IMPROVED)
# -------------------------------
def risk_level(row):
    if row["performance_score"] < 60:
        return "High Risk"
    elif row["performance_score"] < 75:
        return "Medium Risk"
    else:
        return "Low Risk"

data["risk_level"] = data.apply(risk_level, axis=1)

# -------------------------------
# INTERVENTION SYSTEM
# -------------------------------
def intervention(row):
    if row["risk_level"] == "High Risk":
        return "Immediate mentoring, improve attendance, and structured study plan required"
    elif row["risk_level"] == "Medium Risk":
        return "Focus on test preparation and regular revision"
    else:
        return "Maintain current performance and consistency"

data["intervention"] = data.apply(intervention, axis=1)

# -------------------------------
# SUMMARY
# -------------------------------
print("\n===== SUMMARY =====")
print(data["risk_level"].value_counts().reindex(
    ["High Risk", "Medium Risk", "Low Risk"], fill_value=0).to_string()
)

class_avg = data["average_score"].mean()
print("\nClass Average Score:", round(class_avg, 2))

# -------------------------------
# COURSE ANALYSIS
# -------------------------------
course_avg = data.groupby("course_code")["average_score"].mean()

print("\n===== COURSE ANALYSIS =====")
print(course_avg.to_string())

print("\nBest Performing Course:", course_avg.idxmax())
print("Lowest Performing Course:", course_avg.idxmin())

# -------------------------------
# HIGH RISK STUDENTS
# -------------------------------
print("\n===== HIGH RISK STUDENTS =====")

high_risk = data[data["risk_level"] == "High Risk"]

for _, row in high_risk.iterrows():
    print(f"{row['name']} → {row['intervention']}")

# -------------------------------
# TOP PERFORMERS
# -------------------------------
print("\n===== TOP PERFORMERS =====")

top_students = data.sort_values(by="performance_score", ascending=False).head(5)

for _, row in top_students.iterrows():
    print(f"{row['name']} → Score: {round(row['performance_score'], 2)}")

# -------------------------------
# GRAPH 1: Risk Distribution (FIXED)
# -------------------------------
plt.figure(figsize=(6,4))

risk_counts = data["risk_level"].value_counts().reindex(
    ["High Risk", "Medium Risk", "Low Risk"], fill_value=0
)

risk_counts.plot(kind="bar")

plt.title("Student Risk Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()

# -------------------------------
# GRAPH 2: ALL STUDENTS PERFORMANCE (IMPROVED)
# -------------------------------
plt.figure(figsize=(14,6))

# Sort for better readability
sorted_data = data.sort_values(by="average_score")

plt.bar(sorted_data["name"], sorted_data["average_score"])

plt.axhline(y=class_avg, linestyle='--')

plt.xticks(rotation=60, ha='right')

plt.xlabel("Students")
plt.ylabel("Average Score")
plt.title("Student Performance (All Students)")

plt.tight_layout()
plt.show()

# -------------------------------
# GRAPH 3: COURSE PERFORMANCE
# -------------------------------
course_avg.plot(kind="bar")

plt.xlabel("Course")
plt.ylabel("Average Score")
plt.title("Course-wise Performance Analysis")

plt.tight_layout()
plt.show()