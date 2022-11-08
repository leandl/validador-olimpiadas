from src.validator import Validator
from src.question import Question
from src.test import Test

JSON_QUESTIONS = {
    "question_1": {
        "name": "Somar",
        "tests": [
            {
                "agrs": [1, 5],
                "result": 6
            },
            {
                "agrs": [2, 7],
                "result": 9
            },
            {
                "agrs": [3, 1],
                "result": 4
            },
            {
                "agrs": [-1, 2],
                "result": 1
            }
        ]
    }
}


if __name__ == "__main__":
    questions_in_json = JSON_QUESTIONS
    questions = {}

    for key_question, question in questions_in_json.items():
        tests = [Test(test.get("agrs"), test.get("result")) for test in question["tests"] ]
        questions[key_question] = Question(key_question, tests)


    validator = Validator(questions)
    validator.test("question_1")

 