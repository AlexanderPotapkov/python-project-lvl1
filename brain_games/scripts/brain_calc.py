#!/usr/bin/env python

"""This script start the game 'Brain-valc'"""

from brain_games.engine import welcome_user
from brain_games.games import brain_calc


def main():
    """
    Program run.

    Parameters are missing.

    Returns: None
    """
    welcome_user(brain_calc)


if __name__ == '__main__':
    main()

