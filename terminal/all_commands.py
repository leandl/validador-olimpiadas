import os
from typing import List

from entities.list_commands import ListCommands
from entities.supportted_langs import SupporttedLangs
from config import Config

list_commands = ListCommands()

def valid_support_lang(lang: str):
  return lang in SupporttedLangs.all_langs()


@list_commands.add(["-h"])
@list_commands.add(["--help"])
def helper(_args: List[str]):
  return (
    "STRING",
    """commands:
    -h | retorna os comandos,
    test <lang-option> all | executa todos os testes"""
  )

@list_commands.add(["test", valid_support_lang, "all"])
def validator_all(args: List[str]):
  return (
    "NAO-SEI",
    args
  )

@list_commands.add(["generate", "setup", valid_support_lang])
def generate_setup(args: List[str]):
  lang = args[2]
  path_file_generate_setup = Config.path["GENERATE-SETUP"] + "/main.py"

  response = str((os.popen(f"python3 {path_file_generate_setup} --lang={lang}").read()))
  return (
    "NAO-SEI",
    response
  )


@list_commands.add_command_invalid
def command_invalid(_args: List[str]):
  return (
    "ERROR-STRING",
    _args
  )