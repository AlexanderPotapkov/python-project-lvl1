#!/usr/bin/env python

"""This script start the game 'Brain-even'."""

from brain_games.game_engine import welcome_user
from brain_games.games import even


def main():
    welcome_user(even)


if __name__ == '__main__':
    main()
