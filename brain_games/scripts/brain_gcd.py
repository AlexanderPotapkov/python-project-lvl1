#!/usr/bin/env python

"""This script start the game 'Brain-calc'."""

from brain_games.engine import welcome_user
from brain_games.games import brain_gcd


def main():
    """
    Program run.

    Parameters are missing.

    Returns: None
    """
    welcome_user(brain_gcd)


if __name__ == '__main__':
    main()
