from typing import List, Union, Callable
from .command import Command

class ListCommands:

  def __init__(self) -> None:
    self.__commands = []
    self.__command_invalid = None


  def add(self, args: List[Union[str, Callable[[str], bool]]]) -> None:
    def decorator(action):
      command = Command(args, action)
      self.__commands.append(command)

      return action

    return decorator


  def add_command_invalid(self, action):
    command = Command([], action)
    self.__command_invalid = command

    return action

  def get_commands(self):
    return self.__commands


  def get_command_invalid(self):
    return self.__command_invalid