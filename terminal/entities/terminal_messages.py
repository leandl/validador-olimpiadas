from .bcolors import BColors

class TerminalMessages:
  
  @staticmethod
  def success(message):
    print(BColors.OKGREEN + message + '\x1b[0m')

  @staticmethod
  def error(message):
    print(BColors.FAIL + message + '\x1b[0m')

  @staticmethod
  def message(message):
    print(message) 