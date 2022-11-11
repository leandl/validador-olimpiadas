import os
import json

def terminal_error(message):
    print('\x1b[0;37;41m' + message + '\x1b[0m')

supported_langs = ['php', 'python', 'py', 'javascript', 'js']

if __name__ == "__main__":
    x = True
    while (True):
        command = input('Terminal> ')
        
        if not command: 
            terminal_error("Command not found");
            continue
        
        args = command.split(' ')
        
        if len(args) == 2 and args[1] == 'all':
            language = args[0]
            argsExec = 'test_all'
        elif len(args) == 3:
            language = args[0]
            question = args[1]
            method   = args[2]

            if language not in supported_langs:
                terminal_error("Language not supported")
                continue
            argsExec = question + ' ' + method
        else:
            terminal_error("Invalid format");
            continue


        if language == 'php':
            command = f'php php-validator-olympics/main.php {argsExec}'
        elif language == 'javascript' or language == 'js':
            command = f'npm run start javascript-validator-olympics {argsExec}'
        elif language == 'python' or language == 'py':
            command = f'python3 python-validator-olympics/main.py {argsExec}'

        response = str((os.popen(command).read()))
        r = json.loads(response)
        if not r:
            terminal_error('Erro')
            continue
        string_response = ''
        for question in r: 
            for data in r[question]:
                string_response += f"""
                                        Args: {data['args']}\n
                                        Results: {data['results']}
                                    """
        print(string_response)
