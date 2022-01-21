"""Function of the game 'Brain-gcd'."""

from math import gcd
from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_solution():
    """
    Get math expression (question) and correct answer.

    Parameters are missing.

    Returns:
        tuple: str
    """
    number0 = randint(1, 100)
    number1 = randint(1, 100)

    correct_answer = gcd(number0, number1)
    question = '{0} {1}'.format(number0, number1)

    return question, str(correct_answer)
