"""Function of the game 'Brain-progression'."""

from random import choice, randint

GAME_RULE = 'What number is missing in the progression?'
MIN_FIRST_TERM_OF_ARITHMETIC_PROGRESSION = 1
MAX_FIRST_TERM_OF_ARITHMETIC_PROGRESSION = 5
MIN_TERM_OF_ARITHMETIC_PROGRESSION = 50
MAX_TERM_OF_ARITHMETIC_PROGRESSION = 100
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 5
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def get_arithmetic_progression(
        first_term_of_arithmetic_progression,
        initial_term,
        common_difference,
        progression_length):
    progression = list(range(
        first_term_of_arithmetic_progression,
        initial_term, common_difference))[:progression_length]
    return progression


def get_question_and_solution():
    first_term_of_arithmetic_progression = randint(
        MIN_FIRST_TERM_OF_ARITHMETIC_PROGRESSION,
        MAX_FIRST_TERM_OF_ARITHMETIC_PROGRESSION)
    initial_term = randint(
        MIN_TERM_OF_ARITHMETIC_PROGRESSION,
        MAX_TERM_OF_ARITHMETIC_PROGRESSION)
    common_difference = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    progression_length = randint(
        MIN_PROGRESSION_LENGTH,
        MAX_PROGRESSION_LENGTH)
    progression = get_arithmetic_progression(
        first_term_of_arithmetic_progression,
        initial_term,
        common_difference,
        progression_length)
    hidden_term = choice(progression)
    question = progression
    for index, sequence in enumerate(question):
        if sequence == hidden_term:
            question[index] = '..'
        else:
            question[index] = str(sequence)
    return ' '.join(question), str(hidden_term)
