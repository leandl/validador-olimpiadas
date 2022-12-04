from typing import List

from .command import Command
from .list_commands import ListCommands
from .terminal_messages import TerminalMessages
from .show_test import ShowTest

message_type = {
  "DEFAULT": TerminalMessages.message,
  "ERROR" : TerminalMessages.error,
  "SUCCESS" : TerminalMessages.success,
  "SHOW-ALL-TEST": ShowTest.all_test,
  "SHOW-UNIT-TEST": ShowTest.unit_test,
  "SHOW-UNIT-TEST-DETAIL": ShowTest.unit_test_detail,
}

class Terminal:

  def __init__(self, list_commands: ListCommands) -> None:
    self.__commands = list_commands.get_commands()
    self.__command_invalid = list_commands.get_command_invalid()

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
      for command in commands
      if len(command.get_args()) == len(args)
    ]
  
    for command in command_valids:
      if self.__check_command_valid_by_args(args, command):
        return command

    return self.__command_invalid
  
  def run(self):
    while True:
      command = input('Terminal> ')
      args = command.strip().split(' ')
          
      command = self.get_command_by_args(args)
      action = command.get_action()

      t, result = action(args)
      show_messge = message_type.get(t, message_type["DEFAULT"])
      show_messge(result)