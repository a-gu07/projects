import sys
import numpy as np

def main():
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} arg1")
        sys.exit(1)
    rounds = int(sys.argv[1])
    rng = np.random.default_rng()
    doors = np.zeros((rounds, 3))
    prize_indexes = rng.integers(low = 0, high = 2, size = rounds, endpoint = True)
    doors[np.arange(rounds), prize_indexes] = 1
    initial_pick = rng.integers(low=0, high=2, size=rounds,endpoint=True)
    picked = doors[np.arange(rounds), initial_pick] 
    wins = np.sum(picked==0)
    print(f"Out of {rounds} swaps, the prize was found {wins} times. ")

#be warry of trying any number of rounds > 100000000(8 zeros), it may not run 
if __name__ == "__main__":
    main()