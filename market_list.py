# this is an app that holds a list of market items
market_list = []
item_count = 0
option = ' '
while option != 'e':
    if option == '' or option == ' ':
        print('WELCOME TO MARKIT')
        print('Type a - to start adding your list')
        print('Type p - to print the market list')
        print('Type e - to exit the market list')
        option = str(input('> '))
        option = option.lower()
    else:
        while option == 'a':
            print('Press enter after typing every item')
            new_input = str(input(
                'What will you be adding (press "WWW" and hit enter to exit list): '))
            new_input = new_input.lower()
            if new_input == 'www':
                print('')
                print('')
                print('Exiting market list')
                print('Done')
                print('Printing list......')
                print('')
                print('')
                print('YOUR MARKET LIST')
                n = 0
                count = 0
                for n in market_list:
                    count += 1
                    print(f'{count}. {n}')
                option = 'e'
                break
            else:
                item_count += 1
                market_list.append(new_input)
                print(f"{item_count} {market_list}")
        if option == 'p':
            option = 'e'
            if market_list == []:
                print('No list was added')
            else:
                print(market_list)
