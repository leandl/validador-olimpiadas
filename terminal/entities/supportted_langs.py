from enum import Enum

class SupporttedLangs(Enum):
  JAVASCRIPT = "javascript"
  PYTHON = "python"
  PHP = "php"

  @staticmethod
  def all_langs(): 
    return [
      SupporttedLangs.JAVASCRIPT.value,
      SupporttedLangs.PHP.value,
      SupporttedLangs.PYTHON.value
    ]
  