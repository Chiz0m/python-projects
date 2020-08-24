# this is a car game that starts and stops the car

print('type help to see options')
command = ""
while command != 'quit':
    command = input('>')
    command = command.lower()
    if command == 'quit':
        break
    elif command == 'start':
        print('Car started')
        command = ""
    elif command == 'stop':
        print('Car stopped')
        command = ""
    elif command == 'help':
        print('start - to start car')
        print('stop - to stop car')
        print('quit - to exit')
        command = ""
    else:
        print("I don't understand")
