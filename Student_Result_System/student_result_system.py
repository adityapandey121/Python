import logging

LOG_LEVEL = logging.DEBUG

logging.basicConfig(
    filename="student_app.log",
    level=LOG_LEVEL,
    format="%(levelname)s: %(message)s"
)


def calculate_average(marks):
    return sum(marks) / len(marks)


def get_result(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Very Good"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"


def get_number_of_subjects():
    while True:
        try:
            number = int(input("Enter number of subjects: "))

            if number < 0:
                print("Please enter a positive number.")
                logging.warning("Negative number of subjects entered.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            logging.error("Invalid number of subjects entered.")
            continue

        else:
            logging.info("Number of subjects received.")
            return number


def get_marks(number_of_subjects):
    marks = []

    for i in range(number_of_subjects):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1}: "))

                if mark < 0 or mark > 100:
                    raise ValueError

            except ValueError:
                print("Marks must be between 0 and 100.")
                print("Please enter the marks again.")
                logging.error("Invalid marks entered.")
                continue

            else:
                marks.append(mark)
                logging.info("Marks entered successfully.")

                if mark < 50:
                    logging.warning("Mark is below passing range.")

                elif mark < 60:
                    logging.warning("Mark is close to the minimum passing mark.")

                break

    return marks


def process_student():
    logging.info("Student processing started.")

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        logging.warning("Empty student name entered.")
        return

    logging.info("Student name received.")

    number_of_subjects = get_number_of_subjects()

    try:
        if number_of_subjects == 0:
            raise ZeroDivisionError("Number of subjects cannot be zero.")

        marks = get_marks(number_of_subjects)

        if number_of_subjects > 0 and not marks:
            logging.critical("Student processing failed: no marks were received.")
            return

        average = calculate_average(marks)
        logging.debug("Average calculated: %.2f", average)

        result = get_result(average)
        logging.info("Calculation completed.")

        print("\n----- Student Result -----")
        print("Student Name :", name)
        print(f"Average : {average:.2f}")
        print("Result :", result)

        print("\n----- Student Statistics -----")
        print("Highest Mark :", max(marks))
        print("Lowest Mark :", min(marks))
        print(f"Average Mark : {average:.2f}")
        print("Result :", result)

        logging.info("Student statistics calculated successfully.")
        logging.info("Student processing completed.")

    except ZeroDivisionError:
        print("Number of subjects cannot be zero.")
        logging.error("ZeroDivisionError: number of subjects is zero.")

    finally:
        print("Processing completed.")
        logging.info("Processing finished.")


def main():
    logging.info("Application started.")

    while True:
        process_student()

        choice = input("\nDo you want to enter another student? (yes/no): ").strip().lower()

        if choice != "yes":
            break

    logging.info("Application completed.")


if __name__ == "__main__":
    main()
