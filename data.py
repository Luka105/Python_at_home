import random


def do_math():
    print("Simple math problems")
    numbers = [random.randint(1, 20) for _ in range(10)]
    answers = []
    grades = []

    for i in range(7):
        operation = random.choice(['*', '-', '+'])
        num1 = numbers[i + 1]
        num2 = numbers[i + 2]
        question = f'What is {num1} {operation} {num2}: '
        answer = int(input(question))
        answers.append(answer)

        if operation == '*':
            correct_answer = num1 * num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 + num2

        if answer == correct_answer:
            grade = 100
            print(f'{i + 1}. Correct!')
        else:
            grade = 0
            print(f'{i + 1}. Incorrect')
        grades.append(grade)

    total = sum(grades)
    average = total / 7

    print("\nYour Score is", round(average), "%\n")


if __name__ == '__main__':
    do_math()


def grades():
    print("\nGrading System\n")
    cijfer = []
    for _ in range(5):
        cijfer.append(_)
    cijfer[1] = int(input("Cijfer 1. "))
    cijfer[2] = int(input("Cijfer 2. "))
    cijfer[3] = int(input("Cijfer 3. "))
    cijfer[4] = int(input("Cijfer 4. "))
    avg = sum(cijfer)/4
    print("Your score is", round(avg), "%")


if __name__ == '__main__':
    grades()
