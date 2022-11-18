import getopt
import sys

class Terminal:

    def __show_usage():
        print(f"validador - Versao: [0.1.0]")
        print('-h, --help                                   | Ajuda')
        print('-v, --version                                | Versao do aplicativo')
        print('-c \{OPTION\}, --config=\{OPTION\}           | Configuracao que sera usada. Ex: /default.env ou /database/full.env')
        print('-e \{OPTION\}, --execute-on-alert=\{OPTION\} | Executar script em alerta? SIM/NAO, padrao NAO.')
    

    def get_params():

        try:
            opts, args = getopt.getopt(sys.argv[1:], 'hvc:e:', ['help', 'version', 'config=', 'execute-on-alert='])

        except getopt.GetoptError as e:
            print('Ocorreu um erro ao identificar os parametros. Erro:[{}]'.format(e))
            sys.exit(2)

        
        name_file_config = False
        execute_on_alert = False

        param = {}
        print(opts)
        for opt, arg in opts:
            param[opt] = arg

        if '-v' in param or '--version' in param:
            print('version: 0.1.0')
            sys.exit(0)

        if '-h' in param or '--help' in param:
            Terminal.__show_usage()
            sys.exit(0)

        if '-c' in param or '--config' in param:
            name_file_config = str(param['-c'] if ('-c' in param) else param['--config'])
            print(f'--config: {name_file_config}')

        
        if '-e' in param or '--execute-on-alert' in param:
            execute_on_alert = str(param['-e'] if ('-e' in param) else param['--execute-on-alert'])
            execute_on_alert = execute_on_alert.upper() == 'SIM'
            print(f"--execute-on-alert: {execute_on_alert}")
        
