"""Function of the game 'Brain-even'."""

from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    return question % 2 == 0


def get_question_and_solution():
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) is True else 'no'
    return question, correct_answer
