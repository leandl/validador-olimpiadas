import json

from src.validator import Validator
from src.question import Question
from src.test import Test

with open("./data.json") as r:
    JSON_QUESTIONS = json.load(r)

if __name__ == "__main__":
    questions_in_json = JSON_QUESTIONS
    questions = {}

    for key_question, question in questions_in_json.items():
        tests = [Test(test.get("args"), test.get("result")) for test in question["tests"] ]
        questions[key_question] = Question(key_question, tests)


    validator = Validator(questions)
    validator.test("question_1")

 