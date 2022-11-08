from types import List
from src.quest import Quest
from prova.question_1 import question_1

question_def = {
    "question_1": question_1
}

class Validador:
    
    def __init_(self, quests: List[Quest]):
        self.__quests: quests


    def test(self, name: str): 
        question_def = self.question_def.get("name", None)

        if not question_def:
            raise Exception("not existis question")

        question_def




