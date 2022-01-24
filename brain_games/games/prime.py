"""Function of the game 'Brain-prime'."""

from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

first_prime_number = 2


def is_prime(question):
    """
    Get number (question) and correct answer.

    Parameters are missing.

    Returns: Bool
    """
    if question < first_prime_number:
        return False
    for i in range(first_prime_number, question // 2 + 1):
        if question % i == 0:
            return False
    return True


def get_question_and_solution():
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return str(question), str(correct_answer)
