import getopt
import sys

class Terminal:

    def __show_usage():
        print(f"validador - Versao: [0.1.0]")
        print('-h, --help                                   | Ajuda')
        print('-v, --version                                | Versao do aplicativo')
        print('-l \{OPTION\}, --lang=\{OPTION\}             | ')
       
    

    def get_params():

        try:
            opts, args = getopt.getopt(sys.argv[1:], 'hvl:', ['help', 'version', 'lang='])

        except getopt.GetoptError as e:
            print('Ocorreu um erro ao identificar os parametros. Erro:[{}]'.format(e))
            sys.exit(2)


        param = {}
        for opt, arg in opts:
            param[opt] = arg

        if '-v' in param or '--version' in param:
            print('version: 0.1.0')
            sys.exit(0)

        if '-h' in param or '--help' in param:
            Terminal.__show_usage()
            sys.exit(0)

        if '-l' in param or '--lang' in param:
            lang = str(param['-l'] if ('-l' in param) else param['--lang'])
        
        return {
            "lang": lang
        }

        
