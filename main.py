
import csv
from pathlib import Path

SUBJECTS = ("English", "Maths", "AI")
MAX_MARKS = 100
PASS_PERCENTAGE = 50
CSV_FILE = Path("student_results.csv")


def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if 0 <= marks <= MAX_MARKS:
            return marks

        print("Marks must be between 0 and 100.")


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def create_student_result():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_marks(subject)

    total = sum(marks.values())
    maximum = len(SUBJECTS) * MAX_MARKS
    percentage = total / maximum * 100
    grade = calculate_grade(percentage)
    status = "Pass" if percentage >= PASS_PERCENTAGE else "Fail"

    return {
        "name": name,
        "english": marks["English"],
        "maths": marks["Maths"],
        "ai": marks["AI"],
        "total": total,
        "maximum_total": maximum,
        "percentage": round(percentage, 2),
        "grade": grade,
        "status": status,
    }


def display_result(result):
    print("\n--- Student Result ---")
    print("Name:", result["name"])
    print("English:", result["english"])
    print("Maths:", result["maths"])
    print("AI:", result["ai"])
    print(f"Total: {result['total']} / {result['maximum_total']}")
    print(f"Percentage: {result['percentage']:.2f}%")
    print("Grade:", result["grade"])
    print("Status:", result["status"])


def save_result(result):
    fields = [
        "name", "english", "maths", "ai", "total",
        "maximum_total", "percentage", "grade", "status"
    ]

    file_exists = CSV_FILE.exists() and CSV_FILE.stat().st_size > 0

    try:
        with CSV_FILE.open("a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            if not file_exists:
                writer.writeheader()
            writer.writerow(result)

        print(f"Result saved in {CSV_FILE.resolve()}")
    except OSError as error:
        print("Could not save result:", error)


def main():
    print("=== STUDENT GRADE CALCULATOR ===")

    while True:
        result = create_student_result()
        display_result(result)
        save_result(result)

        again = input(
            "\nEnter another student? (y/n): "
        ).strip().lower()

        if again != "y":
            print("Thank you for using the program!")
            break


if __name__ == "__main__":
    main()