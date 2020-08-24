# This is a guessing game that can be inproved on. Just gettnig version one on

the_mind = 10
users_guess = 0
chances = 1
end_game = False

while chances <= 3:
    users_guess = input('Guess: ')
    chances += 1
    if users_guess == the_mind:
        print('You win')
        break
else:
    print('Sorry you failed')
