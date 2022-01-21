"""Function of the game 'Brain-calc'."""

from random import randint, choice
from operator import add, sub, mul

GAME_RULE = 'What is the result of the expression?'
OPERATIONS = (('+', add),
              ('-', sub),
              ('*', mul),)


def get_question_and_solution():
    """
    Get math expression (question) and correct answer.

    Parameters are missing.

    Returns:
        tuple: str
    """
    number_0 = randint(1, 10)
    number_1 = randint(1, 10)
    random_operation = choice(OPERATIONS)

    correct_answer = random_operation[1](number_0, number_1)
    question = '{0} {1} {2}'.format(number_0, random_operation[0], number_1)

    return question, str(correct_answer)
