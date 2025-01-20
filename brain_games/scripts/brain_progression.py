# brain_games/scripts/brain_progression.py
from brain_games.games.progression_games import progression_game
from brain_games.engine import run_game

QUESTION = "What number is missing in the progression?"


def main():    
    run_game(progression_game, QUESTION)


if __name__ == "__main__":
    main()
