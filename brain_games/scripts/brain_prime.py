# brain_games/scripts/brain_prime.py
from brain_games.games.prime_games import prime_game
from brain_games.engine import run_game

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():    
    run_game(prime_game, QUESTION)


if __name__ == "__main__":    
    main()
