"""Function of the game 'Brain-calc'."""

from operator import add, mul, sub
from random import choice, randint

GAME_RULE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATIONS = (
    ('+', add),
    ('-', sub),
    ('*', mul),
)


def get_question_and_solution():
    operation_sign, operation = choice(OPERATIONS)
    number_0 = randint(MIN_NUMBER, MAX_NUMBER)
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = operation(number_0, number_1)
    question = '{0} {1} {2}'.format(number_0, operation_sign, number_1)
    return question, str(correct_answer)
