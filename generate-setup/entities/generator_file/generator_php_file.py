from typing import Tuple
from os import path

from .generator_file import GeneratorFile

params_type_in_function = {
  "INTEGER": "int",
  "FLOAT": "float",
  "STRING": "string",
  "BOOLEAN": "bool",
  "INTEGER-ARRAY": "array",
  "FLOAT-ARRAY": "array",
  "STRING-ARRAY": "array",
  "BOOLEAN-ARRAY": "array",
}

params_type_in_description = {
  "INTEGER": "int",
  "FLOAT": "float",
  "STRING": "string",
  "BOOLEAN": "bool",
  "INTEGER-ARRAY": "int[]",
  "FLOAT-ARRAY": "float[]",
  "STRING-ARRAY": "string[]",
  "BOOLEAN-ARRAY": "bool[]",
}

class GeneratorPHPFile(GeneratorFile):

  def __init__(self, path_templates: str) -> None:
    path_template_javascript = path.join(path_templates, "php.template")
    super().__init__(path_template_javascript)

  def __convert_type_in_function(self, param_type):
    return params_type_in_function.get(param_type, "")

  def __convert_type_in_description(self, param_type):
    return params_type_in_description.get(param_type, "unknown")
    
  def __convert_param_function(self, param):
    name = param["name"]
    param_type = self.__convert_type_in_function(param["type"])
    return f"{param_type} ${name}"

  def __convert_params_function(self, params):
    return ", ".join([ self.__convert_param_function(param) for param in params ])

  
  def __convert_param_description(self, param):
    name = param["name"]
    param_type = self.__convert_type_in_description(param["type"])
    description = param["description"]
    return f"${name}: {param_type} - {description}."

  def __convert_params_description(self, params):
    return "\n".join([self.__convert_param_description(param) for param in params])


  def generate(self, number_question: int, question) -> Tuple[str, str]:
    name_file = f"question{number_question}.php"
    name_question = f"question{number_question}"

    name = question["name"]
    description = question["description"]

    description_result = question.get("description-result", "")
    type_result = self.__convert_type_in_function(question["type-result"])

    params_description = self.__convert_params_description(question["params"])
    params_function = self.__convert_params_function(question["params"])

    new_file = self._template.replace("{name}", name)
    new_file = new_file.replace("{description}", description)

    new_file = new_file.replace("{params-description}", params_description)
    new_file = new_file.replace("{type-return}", type_result)
    new_file = new_file.replace("{description-return}", description_result)
    
    new_file = new_file.replace("{name-question}", name_question)
    new_file = new_file.replace("{params}", params_function)

    return name_file, new_file