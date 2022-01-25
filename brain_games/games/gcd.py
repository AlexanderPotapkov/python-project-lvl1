"""Function of the game 'Brain-gcd'."""

from random import randint

RULES_OF_THE_GAME = 'Find the greatest common divisor of given numbers.'


def gcd(number_0, number_1):
    while number_0 != 0 and number_1 != 0:
        if number_0 > number_1:
            number_0 %= number_1
        else:
            number_1 %= number_0
    return number_0 + number_1


def get_question_and_solution():
    number_0 = randint(1, 100)
    number_1 = randint(1, 100)
    correct_answer = gcd(number_0, number_1)
    question = '{0} {1}'.format(number_0, number_1)
    return str(question), str(correct_answer)
