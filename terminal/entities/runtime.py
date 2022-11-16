from config import Config
import json

with open(Config.file["CONFIG"]) as file:
  configs = json.load(file)

class Runtime:
    PHP = configs["run"]["php"]
    PYTHON = configs["run"]["python"]
    JAVASCRIPT = configs["run"]["javascript"]