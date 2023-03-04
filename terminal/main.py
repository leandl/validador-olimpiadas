import readline
from entities.terminal import Terminal
from all_commands import list_commands 
  
if __name__ == "__main__":
  termianl = Terminal(list_commands)
  termianl.run()