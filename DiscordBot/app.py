from main import Question
questions_promt = [
    "Frage? \n (a) Antwort 1 \n (b) Antwort 2 \n (c) Antwort 3 \n\n ",
    "Frage? \n (a) Antwort 1 \n (b) Antwort 2 \n (c) Antwort 3 \n\n ",
    "Frage? \n (a) Antwort 1 \n (b) Antwort 2 \n (c) Antwort 3 \n\n "
]

questions = [
    Question(questions_promt[0], "a"),
    Question(questions_promt[1], "b"),
    Question(questions_promt[2], "c")
]

def run_test(questions):
    score = 0
    for questions in questions:
        answer = 