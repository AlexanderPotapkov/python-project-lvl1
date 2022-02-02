"""Function of the game 'Brain-progression'."""

from random import choice, randint

GAME_RULE = 'What number is missing in the progression?'
MIN_TERM_OF_ARITHMETIC_PROGRESSION = 1
MAX_TERM_OF_ARITHMETIC_PROGRESSION = 100
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 10


def get_arithmetic_progression(term_of_progression, difference):
    progression = list(range(1, term_of_progression, difference))
    answer = choice(progression)
    for index, sequence in enumerate(progression):
        if sequence == answer:
            progression[index] = '..'
        else:
            progression[index] = str(sequence)
    return progression, answer


def get_question_and_solution():
    term_of_progression = randint(
        MIN_TERM_OF_ARITHMETIC_PROGRESSION,
        MAX_TERM_OF_ARITHMETIC_PROGRESSION)
    difference = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    question, correct_answer = get_arithmetic_progression(
        term_of_progression,
        difference)
    return ' '.join(question), str(correct_answer)
