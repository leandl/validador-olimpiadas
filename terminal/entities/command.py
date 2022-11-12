from typing import List, Union, Callable

class Command:

  def __init__(
    self,
    args: List[Union[str, Callable[[str], bool]]],
    action: Callable[[List[str]], any]
  ) -> None:
    self.__args = args
    self.__action = action

  def get_args(self):
    return self.__args

  def get_action(self):
    return self.__action