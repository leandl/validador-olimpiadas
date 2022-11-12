from typing import List

from .command import Command
from .supportted_langs import SupporttedLangs

def valid_support_lang(lang: str):
  return lang in SupporttedLangs.all_langs()

def command_invalid(_args: List[str]):
  return (
    "ERROR-STRING",
    "command invalid"
  )

def helper(_args: List[str]):
  return (
    "STRING",
    "\n".join([
      "commands:"
      "  -h | retorna os comandos",
      "  test <lang-option> all | executa todos os testes"
    ])
  )

def validator_all(args: List[str]):
  return (
    "NAO-SEI",
    args
  )

commands = {
  # "clear": Command(["clear"], clear),
  # "generate-setup": Command(
  #   ["generate", "setup", valid_support_lang],
  #   generate_setup
  # ),
  "help": Command(["-h"], helper),
  "validator-all": Command(["test", valid_support_lang, "all"], validator_all),
  "command-invalid": Command([], command_invalid),
}