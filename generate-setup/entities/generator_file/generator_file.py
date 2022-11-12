class GeneratorFile:

  def __init__(self, path_template: str) -> None:
    with open(path_template, "r") as file_templete:
      self._template = file_templete.read()

  def generate(self, number_question: int, question) -> str:
    pass