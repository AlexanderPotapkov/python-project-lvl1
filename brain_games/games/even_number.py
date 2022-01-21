"""Function of the game 'Brain-even'."""

from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_solution():
    """
    Get an question and correct answer.

    Parameters are missing.

    Returns:
        tuple: (int, str)
    """
    question = randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
