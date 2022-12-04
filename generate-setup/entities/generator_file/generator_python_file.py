from typing import Tuple
from os import path

from .generator_file import GeneratorFile

params_type = {
  "INTEGER": "int",
  "FLOAT": "float",
  "STRING": "str",
  "BOOLEAN": "bool",
  "INTEGER-ARRAY": "List[int]",
  "FLOAT-ARRAY": "List[float]",
  "STRING-ARRAY": "List[str]",
  "BOOLEAN-ARRAY": "List[bool]",
}

class GeneratorPythonFile(GeneratorFile):

  def __init__(self, path_templates: str) -> None:
    path_template_javascript = path.join(path_templates, "python.template")
    super().__init__(path_template_javascript)

  def __convert_type(self, param_type):
    return params_type.get(param_type, "unknown")
    
  def __convert_param_function(self, param):
    name = param["name"]
    param_type = self.__convert_type(param["type"])
    return f"{name}: {param_type}"

  def __convert_params_function(self, params):
    return ", ".join([ self.__convert_param_function(param) for param in params ])

  def __import_typing_list(self, params):
    for param in params:
      if "ARRAY" in param["type"]:
        return "from typing import List\n"
    
    return ""

  
  def __convert_param_description(self, param):
    name = param["name"]
    param_type = self.__convert_type(param["type"])
    description = param["description"]
    return f"{name}: {param_type} - {description}."

  def __convert_params_description(self, params):
    return "\n".join([self.__convert_param_description(param) for param in params])


  def generate(self, number_question: int, question) -> Tuple[str, str]:
    name_file = f"question_{number_question}.py"
    name_question = f"question_{number_question}"

    type_result = self.__convert_type(question["type-result"])
    params_description = self.__convert_params_description(question["params"])
    params_function = self.__convert_params_function(question["params"])
    import_typing_list = self.__import_typing_list(question["params"])

    new_file = self._template.replace("{name}", question["name"])
    new_file = new_file.replace("{description}", question["description"])
    new_file = new_file.replace("{params-description}", params_description)
    new_file = new_file.replace("{type-return}", type_result)
    new_file = new_file.replace("{name-question}", name_question)
    new_file = new_file.replace("{params}", params_function)
    new_file = new_file.replace("{import-typing-list}", import_typing_list)

    return name_file, new_file