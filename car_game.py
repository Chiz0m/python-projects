# this is a car game that starts and stops the car

print('type help to see options')
command = ""
car_started = False
while True:
    command = input('> ')
    command = command.lower()
    if command == 'quit':
        if car_started:
            print('Please type "stop" to stop the car')
        else:
            break
    elif command == 'start':
        if car_started:
            print('Car was already started')
        else:
            print('Car started')
            command = ""
            car_started = True
    elif command == 'stop':
        if car_started:
            print('Car stopped')
            command = ""
            car_started = False
        elif car_started == False:
            print("You already stopped the car initially")
        else:
            print("You can't turn off a car that is not started")
    elif command == 'help':
        print('start - to start car')
        print('stop - to stop car')
        print('quit - to exit')
        command = ""
    else:
        print("I don't understand")
