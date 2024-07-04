from dataclasses import dataclass


# def execute_command(command: str):
#     match command:
#         case 'ls':
#             print('$ listing files')
#         case 'cd':
#             print('$ changing directory')
#         case _: # Não obrigatório
#             print('$ command not implemented')
    
#     print('...rest of the code')

# execute_command('pwd')

# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories] if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL directories from', directory)
#         case ['ls', 'list', *directories] if len(directories) <= 1: # primeiro valor constante, segundo valor é genérico
#             for directory in directories:
#                 print('$ listing files', directory)
#         case['cd' | 'change', *directories]:
#             for directory in directories:
#                 print(' changing directory to', directory)
#         case _: # Não obrigatório
#             print('$ command not implemented')

# execute_command('ls /Users/ --force')

# def execute_command(command):
#     match command:
#         case {'command': 'ls'}:
#             for directory in command['directories']:
#                 print('$ listing ALL directories from', directory)
#         case _:
#             print('$ command not implemented')
    
#     print('...rest of the code')

# execute_command({'command': 'ls', 'directories': []})

@dataclass
class Command:
    command: str
    directories: list[str]

def execute_command(command: Command):
    match command:
        case Command(command=_, directories=[_,*_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case Command(commandd='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case _:
            print('$ command not implemented')
    
    print('...rest of the code')

command_1 = Command('ls', [])
command_2 = Command('cd', ['/users'])
execute_command(command_1)