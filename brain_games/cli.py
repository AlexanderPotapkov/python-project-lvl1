"""This script starts the Brain Games program."""

import prompt


def welcome_user():
    """Return a welcome message."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
