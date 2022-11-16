from os import path, pardir

root_dirname = path.abspath(path.join(__file__, pardir))
root_dirname_project_validator = path.abspath(path.join(root_dirname, pardir))
root_dirname_generate_setup = path.abspath(path.join(root_dirname_project_validator, "generate-setup"))

path_file_json_data = path.join(root_dirname_project_validator, "data.json")

class Config:
  path = {
    "ROOT": root_dirname,
    "GENERATE-SETUP": root_dirname_generate_setup
  }

  file = {
    "JSON-DATA": path_file_json_data
  }