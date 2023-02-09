 # AB1.py contains the implementation of the first Alice-Bob protocol

 # Importing necessary modules
import copy
from s4_Semantics.AConfig import AConfig

# Defining the AliceBob class that implements the AConfig class
class AliceBob(AConfig):
    # Constructor for the AliceBob class
    def __init__(self):
        # Alice is represented by 1 and Bob is represented by 2
        self.conf = [[1], [], [2]] 

    # Method to return the configuration
    def config(self):
        return self.conf

    # Method to return a deep copy of the object
    def copy(self):
        return copy.deepcopy(self)

    # Method to check the condition for entry into a specific state
    def AB_on_entry(self, n):
        return len(n.conf[1])>=2

    # Method to define the hash function for the object
    def __hash__(self):
        return 1

    # Method to check equality between two objects
    def __eq__(self, other):
        return self.conf==other.conf

    # Method to return the string representation of the object
    def __repr__(self):
        return str(self.conf)

# Function to return a guard for a specific transition between two states
def guardeAB(i, j):
    def res(config):
        # Check if source and target are the same
        if i == j :
            return False
        # Check if the source state is empty
        if config.conf[i] == []: 
            return False
        # Check if Alice or Bob is at the source state and target is the wait state
        elif i==0 or i==2:
            if j!=1:
                return False
            else :
                return True
        # Check if the wait state is the source and Alice or Bob is in it
        elif i == 1:
            if config.conf[i][0] == 2 and j != 2:
                return False
            if config.conf[i][0] == 1 and j != 0:
                return False
        else :
            return True
    return res

# Function to change the state configuration for a specific transition
def changeAB(i, j):
    def res(config):
        # Pop the item from the source state
        indice = config.conf[i].pop(0)
        # Append the item to the target state
        config.conf[j].append(indice)
        return config

    return res
