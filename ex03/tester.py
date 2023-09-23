from new_student import Student


def main():
    """main() docstring"""
    student = Student(name="Edward", surname="agle")
    print(student)

    try:
        student = Student(name="Edward", surname="agle", id="toto")
        print(student)
    except Exception as e:
        print(e.__class__.__name__ + ":", e)


if __name__ == "__main__":
    main()
