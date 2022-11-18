from os import path, pardir

root_dirname = path.abspath(path.join(__file__, pardir))
root_dirname_project_validator = path.abspath(path.join(root_dirname, pardir))
root_dirname_generate_setup = path.abspath(path.join(root_dirname_project_validator, "generate-setup"))
root_dirname_exam = path.abspath(path.join(root_dirname_project_validator, "exam"))

path_file_json_data = path.join(root_dirname_project_validator, "data.json")
path_file_php_validator = path.join(root_dirname_project_validator, "validator", "php", "main.php")
path_file_json_config = path.join(root_dirname_project_validator, "config.json")

class Config:
  path = {
    "ROOT": root_dirname,
    "GENERATE-SETUP": root_dirname_generate_setup,
    "EXAM": root_dirname_exam
  }

  file = {
    "JSON-DATA": path_file_json_data,
    "CONFIG": path_file_json_config,
    "PHP-VALIDATOR": path_file_php_validator,
  }