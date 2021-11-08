#Name: Lingling Wang, Xiaohan Zhao, Ruixin Li
#Program 3

import numpy as np
from random import choice
import random

river_space = []
# creating a river_space to store B(Bear),F(Fish),N(None)


class River:
    def __init__(self, eco_space=10):
        self.eco_space = eco_space
        self.river_space = [choice("BFN") for x in range(eco_space)]
        # Randomly choose Bear/Fish/None and store it to the river_space.
        # From Stackoverflow: https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly

    def add_bear(self, n):
        if self.river_space[n - 1] == "N":
            self.river_space[n - 1] = "B"
            print("Bear is added!")
            # If a Bear placed in to None space.
        else:
            if self.river_space[n - 1] == "B":
                print("Rejected: Already Occupied by a Bear.")
                # If a Bear meets a Bear, reject
            elif self.river_space[n - 1] == "F":
                print("Bear eats Fish!")
                self.river_space[n - 1] = "B"
                # If a Bear meets a Fish, replace the Fish to Bear

        data.random_move_animal()
        # After the add generate a random move within the list.

    def add_fish(self, n):
        if self.river_space[n - 1] == "N":
            self.river_space[n - 1] = "F"
            print("Fish is added!")
            # If a Fish placed in to a None space.
        else:
            if self.river_space[n - 1] == "B":
                print("Bear eats Fish!")
                # If a Fish meets a Bear, Bear stay
            elif self.river_space[n - 1] == "F":
                print("Rejected: Already Occupied by a Fish.")
                # If a Fish meets a Fish, reject

        data.random_move_animal()
        # After add, generate a random move within the list.

    def get_eco(self):
        print(self.river_space)
        print("Number of Bears:", self.river_space.count("B"))
        print("Number of Fishes:", self.river_space.count("F"))
        # Count the Bears and Fishes through number of the count.

    def kill(self, n):
        if self.river_space[n - 1] == "B" or self.river_space[n - 1] == "F":
            self.river_space[n - 1] = "N"
            # Kill any B or F and replace it with N.
            data.random_move_animal()
        else:
            print("Nothing is here, no animal is killed.")
            data.random_move_animal()

    def random_move_animal(self):
        try:
            position = 0
            while position < 10:
                # (-1 = move left), (0 = no move), (1 = move right)
                if position == 0:
                    move = choice([0, 1])
                    # when pos = 0, means the first F/B/N can only move to right or stay
                elif position == 9:
                    move = choice([-1, 0])
                    # when pos = 9, means the last F/B/N can only move to left or stay
                else:
                    move = choice([-1, 0, 1])
                    # all other F/B/N can move right, left or stay.

                new_move = position + move
                if self.river_space[position] == "F":  # If the moving animal is fish.
                    if (
                        self.river_space[new_move] == "N"
                    ):  # If the animal in new position is None.
                        self.river_space[
                            position
                        ] = "N"  # The original position is None.
                        self.river_space[new_move] = "F"  # The new position is fish.
                        if move == 1:  # If it move to the right
                            position += 2  # We will skip the next position.
                            # prevent move again

                        else:  # If it stays or moves to the left.
                            position += 1

                    elif (
                        self.river_space[new_move] == "B"
                    ):  # If the animal in new position is Bear.
                        self.river_space[
                            position
                        ] = "N"  # The original position is None. The new position doesn't change.
                        position += 1  # Go to the next position.
                        # eaten by bear
                    elif self.river_space[new_move] == "F":
                        position += 1  # If the animal in new position is also fish.
                        if move != 0:
                            data.fish_baby()  # Get a new baby fish.
                            # have a baby somewhere in N
                        else:
                            pass

                elif self.river_space[position] == "B":  # If the moving animal is bear.
                    if (
                        self.river_space[new_move] == "N"
                    ):  # If he animal in new position is None
                        self.river_space[
                            position
                        ] = "N"  # The original position is None.
                        self.river_space[new_move] = "B"  # The new position is bear.
                        if move == 1:  # If it moves to the right
                            position += 2  # Skip the next position
                            # prevent move again

                        else:  # Stay or move to the left.
                            position += 1

                    elif (
                        self.river_space[new_move] == "F"
                    ):  # If the animal in new position is fish.
                        self.river_space[
                            position
                        ] = "N"  # The original position is None.
                        self.river_space[new_move] = "B"  # The new position is bear.
                        if move == 1:  # If it moves to the right
                            position += 2  # Skip the next position
                            # eats fish and prevent move again
                        else:  # Stay or move to the left.
                            position += 1

                    elif (
                        self.river_space[new_move] == "B"
                    ):  # If the animal in the new position is also bear
                        position += 1
                        if move != 0:
                            data.bear_baby()
                            # have a baby somewhere in N
                        else:
                            pass
                else:  # If the moving animal is None
                    position += 1  # Don't do anything and go to the next position.

        except IndexError:
            pass

    def fish_baby(self):
        if len(self.river_space) == 10 and "N" in self.river_space:
            # when the length of the river_space is 10 and N in the river space
            if self.river_space.count("N") == 1:
                # handle only 1 N left
                for index, elem in enumerate(self.river_space):
                    if elem == "N":
                        self.river_space[index] = "F"
                # replace the N with F to genereate a fish baby.
                # From StackOverflow: https://stackoverflow.com/questions/45774519/how-to-replace-a-word-to-another-word-in-a-list-python
            else:
                self.river_space.remove("N")
                # for any case with more N in the river space.
                random_baby = random.randint(0, len(self.river_space))
                self.river_space = (
                    self.river_space[:random_baby]
                    + ["F"]
                    + self.river_space[random_baby:]
                )
                # randomly select a place to place the Fish baby into the river space.
                # from stackoverflow: https://stackoverflow.com/questions/62001466/insert-characters-randomly-into-string-array-a-minimum-amount-of-times

    def bear_baby(self):
        if len(self.river_space) == 10 and "N" in self.river_space:
            # when the length of the river_space is 10 and N in the river space
            if self.river_space.count("N") == 1:
                # handle only 1 N left
                for index, elem in enumerate(self.river_space):
                    if elem == "N":
                        self.river_space[index] = "B"
                # replace the N with F to genereate a fish baby.
            else:
                # for any case with more N in the river space.
                self.river_space.remove("N")
                random_baby = random.randint(0, len(self.river_space))
                if "N" in self.river_space:
                    self.river_space = (
                        self.river_space[:random_baby]
                        + ["B"]
                        + self.river_space[random_baby:]
                    )
                    # randomly select a place to place the Fish baby into the river space.


if __name__ == "__main__":
    data = River()
    print("Adding a fish or a bear!")
    data.get_eco()

    #data.add_bear(2)
    #data.add_fish(3)
    #data.kill(4)
    #data.random_move_animal()
    #data.get_eco()

#-------------------------------------------------------------------------------------------
def Min(s):
    return s[0] if len(s) ==1 else min(float(s[0]),float(Min(s[1:])))
#if only one number then return that number, else find min
def Max(s):
    return s[0] if len(s) ==1 else max(float(s[0]),float(Max(s[1:])))
#if only one number then return that number, else find max
if __name__ == "__main__":
  print("Question 2")
  print("For question 2, please separate the numbers with space. example: 1 234 56 7890")
  try:
      text = input().split()
      print('Min:',Min(text))
      print('Max:',Max(text))
  except ValueError:
      print("Please input in the correct format")

#-------------------------------------------------------------------------------------------

def Reverse(word):
    return word[-1] if len(word) == 1 else word[-1] + Reverse(word[:-1])
#reverse the word

def palindrome(text):
    try:
        if text == Reverse(text):
            print("Yes, It is palindrome.")
            return True
        else:
            print("No, It is not palindrome.")
            return False
        #test if reversed word is equal to the input text
    except IndexError:
        print("Please try again, and enter any word!")
        pass
    #exception


if __name__ == "__main__":
    w = input("Please enter a string to check if it is palindrome: ")
    palindrome(w)
