import os

from config import Config
from entities.runtime import Runtime

class CommandLine:

  @staticmethod
  def __exec(command: str) -> str:
    return str((os.popen(command).read()))
  
  @staticmethod
  def generate_setup(lang: str) -> str:
    path_file_generate_setup = os.path.join(Config.path["GENERATE-SETUP"], "main.py")
    command = f"{Runtime.PYTHON} \"{path_file_generate_setup}\" --lang={lang}"

    return CommandLine.__exec(command)

  @staticmethod
  def valid_test_php(number_question: int = None) -> str:
    path = Config.file["PHP-VALIDATOR"]
    json_path = Config.file["JSON-DATA"]
    exam_path = Config.path["EXAM"]
    
    command = f"{Runtime.PHP} \"{path}\" --json-data=\"{json_path}\" --exam-path=\"{exam_path}\""
    if number_question:
      command = f"{command} --question=question{number_question}"

    return CommandLine.__exec(command)


  @staticmethod
  def valid_test_javascript(number_question: int = None) -> str:
    path = Config.file["JAVASCRIPT-VALIDATOR"]
    json_path = Config.file["JSON-DATA"]
    exam_path = Config.path["EXAM"]
    
    command = f"{Runtime.JAVASCRIPT} \"{path}\" --json-data=\"{json_path}\" --exam-path=\"{exam_path}\""
    if number_question:
      command = f"{command} --question=question{number_question}"

    return CommandLine.__exec(command)