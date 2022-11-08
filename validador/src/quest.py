from types import List
from src.test import Test

class Question:

    def __init__(self, name: str, tests: List[Test]) -> None:
        self.__name = name
        self.__tests = tests

    def get_name(self) -> str:
        return self.__tests

    def get_tests(self) -> List[Test]:
        return self.__tests



