def get_student_data():
    student_data = {}
    while True:
        name = input("Enter name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            score = int(input("Enter score: "))
            student_data[name] = score
        except ValueError:
            print("Please enter a valid number.")
    return student_data

def calculate_grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 45:
        return "C"
    else:
        return "F"

# Get student data
students = get_student_data()

# Calculate grades
grades = {}
for name, score in students.items():
    grades[name] = calculate_grade(score)

# Show results
print("\nStudent Grades:")
for name, grade in grades.items():
    print(f"{name}: {grade}")

def class_statistics(*scores):
    if not scores:
        return None, None, None  # In case no scores are given
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)
    return minimum, maximum, average
# After you already have the student scores from get_student_data()

min_score, max_score, avg_score = class_statistics(*students.values())

print("\nClass Statistics:")
print(f"Minimum Score: {min_score}")
print(f"Maximum Score: {max_score}")
print(f"Average Score: {avg_score:.2f}")
