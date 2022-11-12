from entities.commands import commands
from entities.terminal import Terminal
  
if __name__ == "__main__":
  termianl = Terminal(commands)
  termianl.run()