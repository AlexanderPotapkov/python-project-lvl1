"""Function of the game 'Brain-progression'."""

from random import choice, randint

RULES_OF_THE_GAME = 'What number is missing in the progression?'


def get_question_and_solution():
    start = randint(1, 10)
    stop = randint(60, 100)
    step = randint(1, 6)
    question = list(range(start, stop, step))

    correct_answer = choice(question)
    for index, sequence in enumerate(question):
        if sequence == correct_answer:
            question[index] = '..'
        else:
            question[index] = str(sequence)

    return ' '.join(question), str(correct_answer)