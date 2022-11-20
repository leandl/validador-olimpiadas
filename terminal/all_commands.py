import os
import sys
from typing import List

from entities.list_commands import ListCommands
from entities.supportted_langs import SupporttedLangs
from entities.command_line import CommandLine

list_commands = ListCommands()

def get_command_line_valid_test_by_lang(lang: str):
  command_line_valid_test = {
    SupporttedLangs.PHP.value: CommandLine.valid_test_php,
    SupporttedLangs.JAVASCRIPT.value: CommandLine.valid_test_javascript,
  }

  return command_line_valid_test.get(lang)

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
  command_line_valid_test = get_command_line_valid_test_by_lang(lang)

  response = command_line_valid_test(question)
  return (
    "ERROR",
    response
  )

@list_commands.add(["test", valid_support_lang, "all"])
def validator_all(args: List[str]):
  lang = args[1]
  command_line_valid_test = get_command_line_valid_test_by_lang(lang)
  
  response = command_line_valid_test()
  return (
    "ERROR",
    response
  )

  
@list_commands.add(["generate", "setup", valid_support_lang])
def generate_setup(args: List[str]):
  lang = args[2]
  response = CommandLine.generate_setup(lang)

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

