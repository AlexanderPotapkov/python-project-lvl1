#!/usr/bin/env python

"""This script start the game 'Brain-progression'."""

from brain_games.game_engine import welcome_user
from brain_games.games import progression


def main():
    welcome_user(progression)


if __name__ == '__main__':
    main()
