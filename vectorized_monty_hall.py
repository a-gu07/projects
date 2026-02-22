import sys
import numpy as np
"""
A program to simulate many runs of the Monty Hall gameshow question. Here, we always swap doors, and 
the final number of successes and success rate are reported. Clearly, probability works!
"""

def main():
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} #number_of_rounds")
        sys.exit(1)
    rounds = int(sys.argv[1])
    rng = np.random.default_rng()
    doors = np.zeros((rounds, 3))
    # generates an array of shape (rounds, ) that contains ints between 1 and 2 inclusive
    prize_indexes = rng.integers(low = 0, high = 2, size = rounds, endpoint = True)
    doors[np.arange(rounds), prize_indexes] = 1
    initial_pick = rng.integers(low=0, high=2, size=rounds,endpoint=True)
    picked = doors[np.arange(rounds), initial_pick] 
    # if you choose a door without a prize, you always swap into the prize door!!
    wins = np.sum(picked==0)
    print(f"Out of {rounds} swaps, the prize was found {wins} times. ")
    print(f"Swapping gives a {float(wins)*100/rounds}% success rate.")

#be warry of trying any number of rounds > 100000000(8 zeros), it may not run 
if __name__ == "__main__":
    main()