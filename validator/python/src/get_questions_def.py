import importlib.util
import os
from src.printer import Printer

def import_module_from_file(full_path_to_module):
  module = None

  try:
    # Get module name and path from full path
    module_dir, module_file = os.path.split(full_path_to_module)
    module_name, module_ext = os.path.splitext(module_file)

    # Get module "spec" from filename
    spec = importlib.util.spec_from_file_location(module_name,full_path_to_module)
    module = spec.loader.load_module()
  except Exception as ec:
    # Simple error printing
    # Insert "sophisticated" stuff here
    print(ec)
  
  return module

def get_questions_def(exam_path: str):
  questions_def = {}

  if not os.path.isdir(exam_path):
    Printer.error("Invalid path specified.")

  files = []
  for _dirname, _dirnames, filenames in os.walk(exam_path):
    for filename in filenames:
      if filename.endswith(".py"):
        files.append(filename)
  
  for file_exam in files:
    path_file_exam = os.path.join(exam_path, file_exam)
    name_question = file_exam.replace(".py", "")

    data_file_exam = import_module_from_file(path_file_exam)
    questions_def[name_question] = getattr(data_file_exam, name_question)

  return questions_def







