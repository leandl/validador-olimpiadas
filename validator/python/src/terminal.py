import getopt
import sys

from src.printer import Printer

class Terminal:
    
    @staticmethod
    def get_params():

        try:
            opts, args = getopt.getopt(sys.argv[1:], 'q::j:e:', ['question=', 'json-data=', 'exam-path='])
        except getopt.GetoptError as e:
            print('Ocorreu um erro ao identificar os parametros. Erro:[{}]'.format(e))
            sys.exit(2)

        param = {}
        args = {}

        for opt, arg in opts:
            param[opt] = arg

        args["question"] = None
        if '-q' in param or '--question' in param:
            args["question"] = str(param['-q'] if ('-q' in param) else param['--question'])

        if '-j' in param or '--json-data' in param:
            args["json-data"] = str(param['-j'] if ('-j' in param) else param['--json-data'])
        else:
            Printer.error('Invalid json path specified.')
        
        if '-e' in param or '--exam-path' in param:
            args["exam-path"] = str(param['-e'] if ('-e' in param) else param['--exam-path'])
        else:
            Printer.error('Invalid exam path specified.')
        
        return args