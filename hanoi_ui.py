# Sami Bensaadi (2026)
# Visual Tower of Hanoi implementation
import time
import os
#  PROBLEM: Move N disks from source peg (LEFT) to target peg (RIGHT)
#  RULES:
#  - Only ONE disk can be moved at a time
#  - A larger disk CANNOT be placed on top of a smaller disk
#  - Use an auxiliary peg (MIDDLE) as helper
#  https://www.geeksforgeeks.org/dsa/c-program-for-tower-of-hanoi/
#
'''STEPS
FUNCTION Hanoi(n, source, target, auxiliary):
    IF n == 1:
        move disk from source → target display state
        RETURN
    # Step 1: --------  move smaller stack away
    Hanoi(n - 1, source, auxiliary, target)
    # Step 2: --------  move largest disk directly
    move disk n from source → target  display state
    # Step 3: --------  move smaller stack onto target
    Hanoi(n - 1, auxiliary, target, source)
END FUNCTION
'''
def display(pegs, n):
    os.system('clear') # clears terminal to repaint in the same entry
    # We print from top level down to bottom level
    for level in range(n - 1, -1, -1):
        # We print all 3 pegs side-by-side
        for peg in ['A', 'B', 'C']:
            # If this peg has a disk at this height
            if len(pegs[peg]) > level:
                disk = pegs[peg][level] # disk size determines width of "=" shape
                print(" " * (n - disk) + "=" * (disk * 2 - 1) + " " * (n - disk), end="  ") # center disk
            else: # else if no disks here, empty rod representation
                print(" " * (n - 1) + "|" + " " * (n - 1), end="  ") 
        print()

    print("-" * (n * 6))
    print("   A        B        C")
    time.sleep(0.5) # slow animation


def hanoi(n, source, target, auxiliary, pegs, total_disks):
    # BASE CASE of recursion:
    # if only 1 disk, move it directly
    if n == 1:
        disk = pegs[source].pop() # remove top disk from source peg (LIFO stack behavior)
        pegs[target].append(disk) # place it on target peg
        display(pegs, total_disks) # show updated state
        return # !!! stop recursion here !!!

    # STEP 1: move n-1 disks out of the way
    hanoi(n - 1, source, auxiliary, target, pegs, total_disks)

    # STEP 2: move largest disk
    disk = pegs[source].pop()
    pegs[target].append(disk)
    display(pegs, total_disks)

    # STEP 3: move n-1 disks onto target
    hanoi(n - 1, auxiliary, target, source, pegs, total_disks)

if __name__ == "__main__":
    disks = 4  # number of disks (problem size)
    # Initial configuration:
    # all disks are on peg A, ordered largest → smallest
    """----------------------------------------------------
    INITIAL STATE:
        source = A
        target = C
        auxiliary = B
        all disks in A (largest at bottom)

    CALL:
    Hanoi(N, A, C, B)-------------------------------------"""

    pegs = {
        'A': list(range(disks, 0, -1)),
        'B': [],
        'C': []
    }
    display(pegs, disks) # show starting state
    # start recursion HERE : move all disks from A → C using B as helper
    hanoi(disks, 'A', 'C', 'B', pegs, disks)
