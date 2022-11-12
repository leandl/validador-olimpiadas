from enum import Enum

class SupporttedLangs(Enum):
  JAVASCRIPT = "javascript"
  PYTHON = "python"
  PHP = "php"

  @staticmethod
  def all_langs(): 
    return [lang.value for lang in (SupporttedLangs)] 
  