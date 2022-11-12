question = {
  "name": "Somatorio",
  "description": "Soma entre a + b",
  "params": [
    {
      "name": "a",
      "type": "INTEGER",
      "description": "Um número qualquer"
    },
    {
      "name": "b",
      "type": "INTEGER",
      "description": "Um número qualquer"
    }
  ],
  "type-result": "INTEGER"
}

def convert_param_function(param):
  name = param["name"]
  param_type = convert_type(param["type"])
  return f"{name}: {param_type}"

def convert_params_function(params):
  return ", ".join([ param["name"] for param in params ])

def convert_type(param_type):
  if param_type == "INTEGER":
    return "number"

  return "string"

def convert_param_description(param):
  name = param["name"]
  param_type = convert_type(param["type"])
  description = param["description"]
  return f"{name}: {param_type} - {description}."

def convert_params_description(params):
  return "\n".join([convert_param_description(param) for param in params])



with open("./question-javascript.template", "r") as file_templete:
  template = file_templete.read()

  new_file = template.replace("{name}", question["name"])
  new_file = new_file.replace("{description}", question["description"])
  new_file = new_file.replace("{type-return}", convert_type(question["type-result"]))
  new_file = new_file.replace("{params}", convert_params_function(question["params"]))
  new_file = new_file.replace("{number-question}", "question1")
  new_file = new_file.replace("{params-description}", convert_params_description(question["params"]))
  


  print(new_file)