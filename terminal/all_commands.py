import os
import sys
from typing import List

from entities.list_commands import ListCommands
from entities.supportted_langs import SupporttedLangs
from config import Config
from entities.runtime import Runtime

list_commands = ListCommands()

def valid_support_lang(lang: str):
  return lang in SupporttedLangs.all_langs()

def valid_question(question: str):
  return question.isnumeric() 

@list_commands.add(["exit"])
def clear(_args: List[str]):
  sys.exit(0)

@list_commands.add(["cls"])
@list_commands.add(["clear"])
def clear(_args: List[str]):
  os.system('cls' if os.name == 'nt' else 'clear')
  return(
    "DEFAULT",
    ""
  )

@list_commands.add(["-h"])
@list_commands.add(["--help"])
def helper(_args: List[str]):
  return (
    "DEFAULT",
    """commands:
    -h | retorna os comandos,
    test <lang-option> all | executa todos os testes"""
  )

@list_commands.add(["test", valid_support_lang, "-question", valid_question])
def validator_all(args: List[str]):
  lang = args[1]
  question = args[3]
  path = Config.file["PHP-VALIDATOR"]
  json_path = Config.file["JSON-DATA"]
  exam_path = Config.path["EXAM"]
  
  response = str(os.popen(f"{Runtime.PHP} \"{path}\" --question=question{question} --json-data=\"{json_path}\" --exam-path=\"{exam_path}\"").read())
  
  return (
    "ERROR",
    response
  )

@list_commands.add(["test", valid_support_lang, "all"])
def validator_all(args: List[str]):
  lang = args[1]
  path = Config.file["PHP-VALIDATOR"]
  json_path = Config.file["JSON-DATA"]
  exam_path = Config.path["EXAM"]
  
  response = str(os.popen(f"{Runtime.PHP} \"{path}\" --json-data=\"{json_path}\" --exam-path=\"{exam_path}\"").read())
  
  return (
    "ERROR",
    response
  )
  
@list_commands.add(["generate", "setup", valid_support_lang])
def generate_setup(args: List[str]):
  lang = args[2]

  path_file_generate_setup = os.path.join(Config.path["GENERATE-SETUP"], "main.py")
  command = f"{Runtime.PYTHON} \"{path_file_generate_setup}\" --lang={lang}"

  response = str((os.popen(command).read()))

  return (
    "DEFAULT",
    response
  )


@list_commands.add_command_invalid
def command_invalid(_args: List[str]):
  command = " ".join(_args)
  return (
    "ERROR",
    f'Invalid Command: {command}'
  )

