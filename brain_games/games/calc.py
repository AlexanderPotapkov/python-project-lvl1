"""Function of the game 'Brain-calc'."""

from operator import add, mul, sub
from random import choice, randint

GAME_RULE = 'What is the result of the expression?'
OPERATIONS = (
    ('+', add),
    ('-', sub),
    ('*', mul),
)


def get_question_and_solution():
    number0 = randint(1, 10)
    number1 = randint(1, 10)
    random_operation = choice(OPERATIONS)

    correct_answer = random_operation[1](number0, number1)
    question = '{0} {1} {2}'.format(number0, random_operation[0], number1)

    return question, str(correct_answer)
