import json

from src.printer import Printer
from src.terminal import Terminal
from src.validator import Validator
from src.generate_data_questions import generate_data_questions
from src.get_questions_def import get_questions_def


if __name__ == "__main__":
    
    dictget = lambda d, *k: [d[i] for i in k]
    question, json_data_path, exam_path = dictget(
        Terminal.get_params(),
        "question", "json-data", "exam-path"
    )
    

    with open(json_data_path) as r:
        JSON_QUESTIONS = json.load(r)
    
    questions = generate_data_questions(JSON_QUESTIONS)
    questions_def = get_questions_def(exam_path)

    validator = Validator(questions, questions_def)
    result = validator.test(question) if question else validator.test_all()

    Printer.success(result)

 