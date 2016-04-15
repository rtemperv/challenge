import threading
from time import sleep
import os

# Layout of the table (P = philosopher, f = fork):
#          P0
#       f3    f0
#     P3        P1
#       f2    f1
#          P2

# Number of philosophers at the table.
# There'll be the same number of forks.
numPhilosophers = 10

# Lists to hold the philosophers and the forks.
# Philosophers are threads while forks are locks.
philosophers = []
forks = []


class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

    def run(self):
        # Left fork has same index as self.index.
        # Right fork has index smaller by 1, except for the first philosopher
        leftForkIndex = self.index
        rightForkIndex = (self.index - 1) if self.index != 0 else (numPhilosophers - 1)

        forkPair = ForkPair(leftForkIndex, rightForkIndex)

        # Eat forever
        while True:
            forkPair.pickUp()
            print("Philosopher", self.index, "eats.")
            forkPair.putDown()


class ForkPair:
    def __init__(self, leftForkIndex, rightForkIndex):
        # Order forks by index
        if leftForkIndex < rightForkIndex:
            self.firstFork = forks[leftForkIndex]
            self.secondFork = forks[rightForkIndex]
        else:
            self.firstFork = forks[rightForkIndex]
            self.secondFork = forks[leftForkIndex]

    def pickUp(self):
        # Pick the fork with lower index first
        self.firstFork.acquire()
        self.secondFork.acquire()

    def putDown(self):
        self.firstFork.release()
        self.secondFork.release()


if __name__ == "__main__":
    # Create our philosophers and forks
    for i in range(0, numPhilosophers):
        philosophers.append(Philosopher(i))
        forks.append(threading.Lock())

    # All philosophers start eating
    for philosopher in philosophers:
        philosopher.start()

    # Allow CTRL + C to exit the program
    try:
        while True: sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)
