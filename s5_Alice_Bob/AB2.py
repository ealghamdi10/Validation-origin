import copy
from s4_Semantics.AConfig import AConfig


class AliceBob2(AConfig):

         # Initializing important variables in the constructor
        def __init__(self):
            self.conf = [[1], [], [], [], [2]]  # Alice and Bob's initial positions
            self.flagAlice = False  # Flag to keep track of Alice's movements
            self.flagBob = False  # Flag to keep track of Bob's movements

         # Method to return the current configuration of Alice and Bob
        def config(self):
            return self.conf

         # Method to create a deep copy of the current configuration
        def copy(self):
            return copy.deepcopy(self)

         # Method to check if Alice and Bob are in the correct positions for Protocol 2
        def AB2_on_entry(self, n):
            return len(n.conf[1]) >= 1 and len(n.conf[3]) >= 1

         # Method to check if all actions are disabled
        def AB2_on_entry2(self, source, n, o):
            print(n)
            return len(list(o[0].enabledActions(n))) == 0  

         # Method to define the hash value for the current configuration
        def __hash__(self):
            return 1

         # Method to check if two configurations are equal
        def __eq__(self, other):
            return self.conf == other.conf

         # Method to return the string representation of the configuration
        def __repr__(self):
            return str(self.conf)

         # Method to define the conditions for Alice and Bob's movements
        def guardeAB2(self, i, j):
            def res(config):
                # Checking if source and destination are the same
                if i == j:
                    return False
                # Checking if source is empty
                if config.conf[i] == []:  #vide
                    return False
                # Checking if source is Alice's position
                elif i == 0:  # alice
                    if j != 1:
                        return False
                    else:
                        self.flagAlice = True
                        return True
                # Checking if source is Bob's position
                elif i == 4:  # bob
                    if j != 3:
                        return False
                    else:
                        self.flagBob = True
                        return True
                # Checking if source is waitAlice
                elif i == 1:  # waitAlice
                    if j != 2 or self.flagBob != False:
                        return False
                    else:
                        return True
                # Checking if source is waitBob
                elif i == 3:  #waitBob
                    if j != 2 or self.flagAlice != False:
                        return False
                    else:
                        return True
                # Checking if source is garden
                elif i == 2:  # jardin
                    if config.conf[i][0] == 2 and j == 4:  # Bob chez Bob
                        self.flagBob = False
                        return True
                    elif config.conf[i][0] == 1 and j == 0:  # Alice chez Alice
                        self.flagAlice = False
                        return True
                    else:
                        return False
                else:
                    return True

            return res



def changeAB2(i, j):
    def res(config):
        indice = config.conf[i].pop(0)
        config.conf[j].append(indice)
        return config

    return res
