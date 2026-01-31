import sys
import numpy as np
from monty_hall import construct_doors, reveal_door

def main():
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} arg1")
        sys.exit(1)
    loops = int(sys.argv[1])

    rng = np.random.default_rng()
    wins = 0
    for i in range(loops):
        doors = construct_doors()
        pick = rng.integers(low=0, high = 2, size = 1, endpoint = True)[0]
        reveal = reveal_door(doors, pick)
        pick = 3-(pick + reveal)
        if (doors[pick]):
            wins+=1
    print(f"Out of {loops} swaps, the prize was found {wins} times. ")

if __name__ == "__main__":
    main()