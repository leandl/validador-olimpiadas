from entities.config import Config
from entities.generator_file.generator_javascript_file import GeneratorJavascriptFile
from entities.generator_file.generator_python_file import GeneratorPythonFile
from entities.generator_file.generator_php_file import GeneratorPHPFile

question = {
  "name": "Somatorio",
  "description": "Soma entre a + b",
  "type-result": "INTEGER",
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
}

generator_file = GeneratorPHPFile(Config.path["TEMPLATES"])
content_file = generator_file.generate(1, question)
print(content_file)
