import sys
import json 

class Printer:

  @staticmethod
  def error(message):
    data_return = {
      "status": "error", 
      "message": message
    }
    
    print(json.dumps(data_return))
    sys.exit(0)


  @staticmethod
  def success(result):
    data_return = {
      "status": "success", 
      "result": result 
    }

    print(json.dumps(data_return))
    sys.exit(0)
