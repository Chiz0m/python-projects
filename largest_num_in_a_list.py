# this app finds the largest number in a list

numbers = [1, 20, 30, 30.1, 39, 50, 69, 7]
memory = 0
for n in numbers:
    if n > memory:
        memory = n
print('Largest number is: ' + str(memory))
