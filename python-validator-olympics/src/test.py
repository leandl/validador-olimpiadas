from typing import List

class Test:

    def __init__(self, args: List[any], result: any) -> None:
        self.__args = args
        self.__result = result

    def get_args(self):
        return self.__args

    def get_result(self):
        return self.__result