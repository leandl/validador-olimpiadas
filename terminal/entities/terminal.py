from typing import Dict, List

from .command import Command

class Terminal:

  def __init__(self, commands: Dict[str, Command]) -> None:
    self.__commands = commands

  def __check_command_valid_by_args(
    self,
    args: List[str],
    command: Command
  ) -> bool:
    command_args = command.get_args()
    
    for index, arg in enumerate(args):
      if isinstance(command_args[index], str):
        if command_args[index] != arg:
          return False
      else:
        valid_test = command_args[index]
        if not valid_test(arg):
          return False

    return True

  def get_command_by_args(self, args: List[str]) -> Command:
    commands = self.__commands
    command_valids = [
      command
      for command in commands.values()
      if len(command.get_args()) == len(args)
    ]
  
    for command in command_valids:
      if self.__check_command_valid_by_args(args, command):
        return command

    return commands["command-invalid"]
  
  def run(self):
    while True:
      command = input('Terminal> ')
      args = command.strip().split(' ')
          
      command = self.get_command_by_args(args)
      action = command.get_action()

      t, result = action(args)
      print(result)