"""Game engine."""

import prompt

NUMBER_OF_ROUNDS = 3


def welcome_user(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game.RULES_OF_THE_GAME)

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_question_and_solution()
        print('Question: {0}'.format(question))
        answer_user = prompt.string('Your answer: ')
        if answer_user == correct_answer:
            print('Correct!')
            continue
        game_over(answer_user, correct_answer, name)
        break
    else:
        print('Congartulations, {0}!'.format(name))


def game_over(answer_user, correct_answer, name):
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer_user, correct_answer))
    print("Let's try again, {0}!".format(name))
