import csv

QUIZ_FILE = "questions.csv"

def read_questions(csv_file):
    questions = []
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                question_text = row[0].strip()
                answer_text = row[1].strip().lower()
                if answer_text == 'true':
                    answer_bool = True
                elif answer_text == 'false':
                    answer_bool = False
                else:
                    continue 
                questions.append((question_text, answer_bool))
    return questions


def read_quiz(questions):
    score = 0
    for i, (question, correct_answer) in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {qusetion}")
        user_input = input("Answer (true/false): ").strip().lower()
        
        if user_input == true:
            user_answer = True
        elif user_input == false:
            user_answer = False
        else:
            print("Incorrect aswer!")
            continue

        if user_answer == correct_answer:
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect answer")
    print(f"\nYour Score: {score} / {len(questions)}")


def main():
    questions = read_questions(QUIZ_FILE)
    run_quiz(questions)


if __name__ == "__main__":
    main()
