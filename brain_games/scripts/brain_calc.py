#!/usr/bin/env python

"""This script start the game 'Brain-calc'."""

from brain_games.game_engine import welcome_user
from brain_games.games import calc


def main():
    welcome_user(calc)


if __name__ == '__main__':
    main()
