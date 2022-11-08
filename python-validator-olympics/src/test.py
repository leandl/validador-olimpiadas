from typing import List

class Test:

    def __init__(self, agrs: List[any], result: any) -> None:
        self.__agrs = agrs
        self.__result = result

    def get_agrs(self):
        return self.__agrs

    def get_result(self):
        return self.__result