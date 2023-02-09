# s5_Alice&Bob



## Alice & Bob Project
This project contains the implementation of two versions of the Alice and Bob problem, as well as a class for representing actions and a class for representing the Interpreted System Semantics (ISS) of the programs.

## Files
The project includes the following files: 
- `AB1.py`: Implements the first version of the Alice and Bob problem, which has 3 places (Alice, garden, Bob).

- `AAB2.py`: Implements the second version of the Alice and Bob problem, which has 5 places (Alice, waitAlice, garden, waitBob, Bob).

- `Action.py`: Implements the Action class, which represents actions in the system.

- `ISS.py`: Implements the ISS class, which represents the Interpreted System Semantics of the program.

## Usage
To use the project, you can import each file in your own project and call their functions as needed. For example, you can create an instance of AliceBob or AliceBob2 and call the config method to get the configuration of the system. You can also call the enabledActions method of the ISS class to get the enabled actions in the system.

## Notes
Note that the Action class is a subclass of MStutter, which is not included in this project. You will need to implement or obtain the MStutter class in order to use the Action class in your project.




