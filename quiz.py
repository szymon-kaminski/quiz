import csv

QUIZ_FILE = questions.csv

def read_questions(csv_file):
    questions = []
    with open(csv_file, newline=' ', encoding='utf-8') as file:
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
