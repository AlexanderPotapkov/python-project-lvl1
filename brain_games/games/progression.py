"""Function of the game 'Brain-progression'."""

from random import choice, randint

GAME_RULE = 'What number is missing in the progression?'
MIN_TERM_OF_ARITHMETIC_PROGRESSION = 50
MAX_TERM_OF_ARITHMETIC_PROGRESSION = 100
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 5
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def get_arithmetic_progression(
        initial_term,
        common_difference,
        progression_length):
    progression = list(range(
        1, initial_term, common_difference))[:progression_length]
    return progression


def stringify_progression(progression, hidden_term_index):
    stringify_progression = progression
    for index, sequence in enumerate(stringify_progression):
        if sequence == hidden_term_index:
            stringify_progression[index] = '..'
        else:
            stringify_progression[index] = str(sequence)
    return stringify_progression


def get_question_and_solution():
    initial_term = randint(
        MIN_TERM_OF_ARITHMETIC_PROGRESSION,
        MAX_TERM_OF_ARITHMETIC_PROGRESSION)
    common_difference = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    progression_length = randint(
        MIN_PROGRESSION_LENGTH,
        MAX_PROGRESSION_LENGTH)
    progression = get_arithmetic_progression(
        initial_term,
        common_difference,
        progression_length)
    hidden_term_index = choice(progression)
    question = stringify_progression(progression, hidden_term_index)
    return ' '.join(question), str(hidden_term_index)
