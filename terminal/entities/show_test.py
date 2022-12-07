import json
from .bcolors import BColors
from .terminal_messages import TerminalMessages

def treat_data(f):
  def wapper_decorator(json_data: str):
    data_terminal = json.loads(json_data)
    if data_terminal.get("status", "error") == "error":
      return TerminalMessages.error(
        data_terminal.get("message", "Ocorreu um erro na execução.")
      )
      

    if not data_terminal.get("result", None):
      return TerminalMessages.error(
        "Não foi possivel obter os dados dos testes"
      )
      
    f(data_terminal.get("result"))
    
  return wapper_decorator

class ShowTest:

  @staticmethod
  @treat_data
  def all_test(data):
    questions = len(data)
    questions_ok = 0

    data_sorted = sorted(data, key=lambda question: question["number"])
    for data_question in data_sorted:
      number_question = data_question["number"]
      question = data_question["data"]

      total_test = len(question)
      total_test_passed = len([test for test in question if test.get("passed", False)])
      
      questions_ok += 1 if total_test == total_test_passed else 0
      porcent = BColors.OKGREEN + "OK" + BColors.DEFAULT if total_test == total_test_passed else f"{total_test_passed}/{total_test}"

      print(f"Questão {number_question}: {porcent}")

    print("==============================")
    print("Tudo OK" if questions == questions_ok else f"{questions_ok}/{questions} questões OK")
      
  @staticmethod
  @treat_data
  def unit_test(question):
    for number_test, test in enumerate(question, start=1):
      if test.get("passed", False):
        OK = BColors.OKGREEN + "OK" + BColors.DEFAULT
        print(f"Teste {number_test}: {OK}")
        continue

      expected_result = test.get("expected_result")
      result = test.get("result")

      TerminalMessages.error("-----------------------------")
      TerminalMessages.error(f"Teste {number_test}:")
      TerminalMessages.error(f"Esperado: {repr(expected_result)}")
      TerminalMessages.error(f"Retorno: {repr(result)}")
      TerminalMessages.error("-----------------------------")
      

  @staticmethod
  @treat_data
  def unit_test_detail(question):
    for number_test, test in enumerate(question, start=1):
      args = ", ".join([repr(arg) for arg in test.get("args")])
      expected_result = repr(test.get("expected_result"))
      result = repr(test.get("result"))
      
      if test.get("passed", False):
        OK = BColors.OKGREEN + "OK" + BColors.DEFAULT
        TerminalMessages.message("-----------------------------")
        TerminalMessages.message(f"Teste {number_test}: {OK}")
        TerminalMessages.message(f"Entrada: {args}")
        TerminalMessages.message(f"Esperado: {expected_result}")
        TerminalMessages.message(f"Retorno: {result}")
        TerminalMessages.message("-----------------------------")
        continue

      TerminalMessages.error("-----------------------------")
      TerminalMessages.error(f"Teste {number_test}:")
      TerminalMessages.error(f"Entrada: {args}")
      TerminalMessages.error(f"Esperado: {expected_result}")
      TerminalMessages.error(f"Retorno: {result}")
      TerminalMessages.error("-----------------------------")