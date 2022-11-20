from src.question import Question
from src.test import Test

def generate_data_questions(json_data_questions):
  questions = []

  for question in json_data_questions:
    tests = [Test(test["args"], test["result"]) for test in question["tests"]]
    questions.append(Question(question["name"], tests))

  return questions
