from random import randint, choice
import sys

MAX_NUM_A = 15
MAX_NUM_B = 5
NEGATIVES_ENABLED = False

q_total = 0
correct = 0

def gen_nums():
    '''
    generate two random numbers
    '''
    a = randint(0,MAX_NUM_A)
    b = randint(0, MAX_NUM_B)
    return a, b

def add(a, b):
    '''
    Return the addition question as a 
    string and the answer as int.
    '''
    question = f'What is {a} + {b}? '
    answer = a + b
    return question, answer

def subtract(a, b):
    '''
    Subtract a from b. If negative answers are
    NOT enabled, it'll keep generating two numbers
    until the answer is a positive.
    '''
    while a - b < 0 and not NEGATIVES_ENABLED:
        a, b = gen_nums()
    question = f'What is {a} - {b}? '
    answer = a - b
    return question, answer

def handle_player_input(q):
    player_input = input(q)
    if player_input.lower() in ('quit', 'exit'):
        print('Bye bye!')
        sys.exit(0)
    else:
        return player_input

def player_answer(q, a):
    '''
    Determine if the player's answer is True or False.
    Then congratulate/commiserate, and display score.
    '''
    while True:
        try:
            guess = handle_player_input(q)        
            guess = int(guess)
            if guess == a:
                print(f'\U00002705 {guess} is correct!')
                return True
            else:
                print('\U0000274C Try again!')
        except ValueError:
            print('You must enter a whole number.')



functions = [add, subtract]

while True:
    a, b = gen_nums()
    random_function = choice(functions)
    q, a = random_function(a, b)
    if player_answer(q, a):
        correct += 1
    q_total += 1
    print(f'Score: {correct}\n')



