"""Function of the game 'Brain-calc'."""

from operator import add, mul, sub
from random import choice, randint

GAME_RULE = 'What is the result of the expression?'
FIRST_NUMBER = randint(1, 10)
SECOND_NUMBER = randint(1, 10)
OPERATIONS = (
    ('+', add),
    ('-', sub),
    ('*', mul),
)


def get_question_and_solution():
    operation_sign, operation = choice(OPERATIONS)

    correct_answer = operation(FIRST_NUMBER, SECOND_NUMBER)
    question = '{0} {1} {2}'.format(FIRST_NUMBER, operation_sign, SECOND_NUMBER)

    return question, str(correct_answer)
