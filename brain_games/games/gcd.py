"""Function of the game 'Brain-gcd'."""

from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd(number_0, number_1):
    while number_0 != 0 and number_1 != 0:
        if number_0 > number_1:
            number_0 %= number_1
        else:
            number_1 %= number_0
    return number_0 + number_1


def get_question_and_solution():
    number_0 = randint(MIN_NUMBER, MAX_NUMBER)
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = gcd(number_0, number_1)
    question = '{0} {1}'.format(number_0, number_1)
    return str(question), str(correct_answer)
