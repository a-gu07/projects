"""
Inspired by the game in CS 2800. A pile of 'n' coins is presented to 2 players, '0' and '1'. On the first move,
player '0' is allowed to take anywhere between '1' and 'n-1' coins from the pile. Then, for every subsequent move 
after, both players are allowed to take between '1' and '2k-1' coins, 'k' being the number of coins taken in the
previous move. The player who takes the remaning coins and reduces the pile to 0 wins. 
Can you find a winning strategy? 
"""

initial = int(input("Enter an initial number: "))
counter = 0
prev = 0
while (initial!=0):
    if (counter==0):
        try:
            decrement = int(input(f"How much does player {counter%2} take? (You can take between 1 and {initial-1}) "))
            if (decrement<1) or (decrement>initial-1):
                print("Invalid amount")
                continue
        except ValueError:
            print("Invalid input")
            continue
    else:
        try:
            capacity = min(2*prev-1, initial)
            decrement = int(input(f"How much does player {counter%2} take? (You can take between 1 and {capacity}) "))
            if (decrement<1) or (decrement>capacity):
                print("Invalid amount")
                continue
        except ValueError:
            print("Invalid input")
            continue
    prev = decrement
    initial-=decrement
    print(f"Amount left: {initial}")
    counter+=1
counter -=1
print(f"Player {counter%2} wins!")