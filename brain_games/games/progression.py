"""Function of the game 'Brain-progression'."""

from random import choice, randint

GAME_RULE = 'What number is missing in the progression?'
MIN_TERM_OF_ARITHMETIC_PROGRESSION = 1
MAX_TERM_OF_ARITHMETIC_PROGRESSION = 20
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 10
LENGTH_OF_PROGRESSION = 10


def get_arithmetic_progression(
        initial_term,
        common_difference):
    return list(range(
        initial_term,
        initial_term + LENGTH_OF_PROGRESSION * common_difference,
        common_difference))


def stringify_progression(progression):
    hidden_term = choice(progression)
    for index, sequence in enumerate(progression):
        if sequence == hidden_term:
            progression[index] = '..'
        else:
            progression[index] = str(sequence)
    return ' '.join(progression), str(hidden_term)


def get_question_and_solution():
    initial_term = randint(
        MIN_TERM_OF_ARITHMETIC_PROGRESSION,
        MAX_TERM_OF_ARITHMETIC_PROGRESSION)
    common_difference = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    progression = get_arithmetic_progression(
        initial_term,
        common_difference)
    question, answer = stringify_progression(progression)
    return question, answer
