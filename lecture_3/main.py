students = []

def input_info():
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add a grade for a student")
    print("3. Show report")
    print("4. Find top performer")
    print("5. Exit")
    return input("Enter your choice: ")


def add_student():
    name = input("Enter student name: ").strip()

    for s in students:
        if s["name"].lower() == name.lower():
            print("This student already exists.")
            return

    students.append({"name": name, "grades": []})
    print("Student added.")


def add_grade():
    name = input("Enter student name: ").strip()

    for s in students:
        if s["name"].lower() == name.lower():

            while True:
                grade_input = input("Enter a grade (or 'done' to finish): ")

                if grade_input.lower() == "done":
                    return

                try:
                    grade = float(grade_input)
                    if 0 <= grade <= 100:
                        s["grades"].append(grade)
                    else:
                        print("Invalid input. Please enter a number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            return

    print("Student not found.")


def show_report():
    print("--- Student Report ---")

    if not students:
        print("No students available.")
        return

    averages = []

    for s in students:
        if len(s["grades"]) == 0:
            print(f"{s['name']}'s average grade is N/A.")
        else:
            avg = sum(s["grades"]) / len(s["grades"])
            averages.append(avg)
            print(f"{s['name']}'s average grade is {avg:.1f}.")

    print("--------------------------------")

    if averages:
        print(f"Max Average: {max(averages):.1f}")
        print(f"Min Average: {min(averages):.1f}")
        print(f"Overall Average: {sum(averages)/len(averages):.1f}")
    else:
        print("No valid grades available.")


def find_top_performer():
    valid = [s for s in students if len(s["grades"]) > 0]

    if not valid:
        print("No valid grades available.")
        return

    top = max(valid, key=lambda s: sum(s["grades"]) / len(s["grades"]))
    avg = sum(top["grades"]) / len(top["grades"])

    print(f"The student with the highest average is {top['name']} with a grade of {avg:.1f}.")

def show_info(choice):
    if choice == "1":
        add_student()
    elif choice == "2":
        add_grade()
    elif choice == "3":
        show_report()
    elif choice == "4":
        find_top_performer()
    elif choice == "5":
        print("Exiting program.")
        return False
    else:
        print("Invalid option.")
    return True


if __name__ == "__main__":
    running = True
    while running:
        running = show_info(input_info())
