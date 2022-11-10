from typing import Dict
from .question import Question

from exam.question_1 import question_1

questions_def = {
    "question_1": question_1
}

class ValidatorException(Exception):
    pass

class Validator:
    
    def __init__(self, questions: Dict[str, Question]):
        self.__questions = questions


    def test(self, name_question: str): 
        question = self.__questions.get(name_question, None)
        question_def = questions_def.get(name_question, None)

        if not question:
            raise ValidatorException("not existis question")

        if not question_def:
            raise ValidatorException("not existis question function")

        for test in question.get_tests():
            print("=====================")
            print(f"Args: {test.get_args()}")
            print(f"Expected Result: {test.get_result()}")

            result = question_def(*test.get_args())
            print(f"Result: {result}")










