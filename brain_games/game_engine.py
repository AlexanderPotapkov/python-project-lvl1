"""Game engine."""

import prompt

NUMBER_OF_ROUNDS = 3


def welcome_user(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game.GAME_RULE)

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_question_and_solution()
        print('Question: {0}'.format(question))
        answer_user = prompt.string('Your answer: ')
        if answer_user == correct_answer:
            print('Correct!')
            continue
        elif answer_user != correct_answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                answer_user, correct_answer))
            print("Let's try again, {0}!".format(name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
