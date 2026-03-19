from random import randint, choice
import logo_maker
import sys

MAX_NUM_A = 10
MAX_NUM_B = 5
NEGATIVE_ANSWERS = True

q_total = 0
score = 0

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
    while a - b < 0 and not NEGATIVE_ANSWERS:
        a, b = gen_nums()
    question = f'What is {a} - {b}? '
    answer = a - b
    return question, answer

functions = (add, subtract)

print(f"""{logo_maker.logo('''Eva's Maths Game''', '''It's positively fun''')}
    Type 'quit' or 'exit' to, you guessed it, quit or exit.
    Type 'negs' to enable/disable sums with negative answers.
    """)
while True:
    a, b = gen_nums()
    random_function = choice(functions)
    question, answer = random_function(a, b)
    q_total += 1
    while True:
        guess = input(question)
        if guess.lower() in ('quit', 'exit'):
            print('Bye bye! \U0001F44B')
            sys.exit(0)
        elif guess.lower() == 'negs':
            if NEGATIVE_ANSWERS:
                NEGATIVE_ANSWERS = False
                print('Negative answers disabled')
            else:
                NEGATIVE_ANSWERS = True
                print('Negative answers enabled')
        else:
            try:
                guess = int(guess)
            except ValueError:
                print('You must enter a whole number \U0001F92E')
        if guess == answer:
            print(f'{guess} is correct! \U00002705')
            score += 1
            print(f'Score: {score}\n')
            break
        elif type(guess) == int:
            print('Try again! \U0000274C')
