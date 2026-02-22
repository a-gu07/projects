import numpy as np

"""
Simulates the monty hall gameshow problem, in which there are 3 doors, 1 of which contains a prize
The contestant chooses a door, and the host reveals one of the 2 doors to be empty. The contestent 
is then offered a choice to switch doors. Should you do it?
"""
def construct_doors():
    rng = np.random.default_rng()
    doors = np.zeros((3,))
    # generates an array of length contiang an 1integer in between 0 and 2 inclusive
    which_door = rng.integers(low=0, high = 2, size = 1, endpoint = True)
    doors[which_door[0]] = 1
    contains = (doors > 0)
    return contains

def reveal_door(arr, choice):
    # reveals one of the doors, which cannot be the door the contestant chose or the prize door
    # can probably be improved using a mask (?)
    for i in range(3):
        if (arr[i] == False and i!= choice):
            return i

def main():
    count = 0
    tally = 0
    wins = 0
    while(True):
        doors = construct_doors()
        choice = input("Which door do you pick(1-3)? ")
        if (choice == 'q'):
            break
        choice = int(choice) -1
        reveal = reveal_door(doors, choice)
        print(f"Door {reveal+1} has nothing inside. Do you switch your pick? ")
        swap = input().lower()
        if (swap == 'y'):
            # sum of indices 0,1,2 is 3, subtracting the 2 indices gives the unrevealed unchosen door
            choice = 3-(choice + reveal)
            tally+=1
        if (doors[choice] and swap=='y'):
            print("You found the prize!")
            wins +=1
        elif (doors[choice] and swap!='y'):
            print("You found the prize!")
        else:
            print("You didn't find the prize.")
        count+=1
    print(f"You swapped {tally} times out of {count} rounds and won {wins} times.")


if __name__ == "__main__":
    # enter 'q' to quit and 'y' to swap
    main()