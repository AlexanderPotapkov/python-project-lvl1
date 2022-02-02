"""Function of the game 'Brain-even'."""

from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(question):
    return question % 2 == 0


def get_question_and_solution():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(question) else 'no'
    return str(question), str(correct_answer)
