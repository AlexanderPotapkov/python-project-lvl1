#!/usr/bin/env python

"""This script start the game 'Brain-even'."""

from brain_games.engine import welcome_user
from brain_games.games import even_number


def main():
    """
    Program run.

    Parameters are missing.

    Returns: None
    """
    welcome_user(even_number)


if __name__ == '__main__':
    main()
