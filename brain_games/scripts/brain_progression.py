#!/usr/bin/env python

"""This script start the game 'Brain-progression'."""

from brain_games.engine import welcome_user
from brain_games.games import progression


def main():
    """
    Program run.

    Parameters are missing.

    Returns: None
    """
    welcome_user(progression)


if __name__ == '__main__':
    main()
