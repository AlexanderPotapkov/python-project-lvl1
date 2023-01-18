"""Function of the game 'Brain-prime'."""

from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER_FOR_QUESTION = 1
MAX_NUMBER_FOR_QUESTION = 100
FIRST_PRIME_NUMBER = 2


def is_prime(number):
    if number < FIRST_PRIME_NUMBER:
        return False
    for i in range(FIRST_PRIME_NUMBER, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_solution():
    number = randint(MIN_NUMBER_FOR_QUESTION, MAX_NUMBER_FOR_QUESTION)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), str(correct_answer)
