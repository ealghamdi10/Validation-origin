# s4_Semantics

This repository contains the source code for a simple program execution model using the "Soup" semantics.

## Purpose
This repository allows to model and simulate a program execution and its associated transition relation.

## Contents
- AConfig.py: this file contains the class AConfig which is an abstract class for configuration classes. It provides a method "copy" to make deep copies of a configuration.

- Rule.py: this file contains the class Rule which represents a rule of the program. It has three attributes: name, guard and action. It has two methods: execute and __str__.

- S_Program.py: this file contains the class SoupProgram which represents a program. It has two attributes: ini and rules. It has one method: add.

- S_Semantics.py: this file contains the class SoupSemantics which is a sub class of SemanticTransitionRelation. It provides the semantics of the program execution by implementing the three methods: initialConfigurations, enabledActions and execute.

- Str2Tr.py: this file contains the class Str2Tr which is a sub class of TransitionRelation. It provides an implementation of the transition relation associated to the program execution.

- cnf1.py: this file contains the class Config1 which is a sub class of AConfig. It provides an example of a configuration class for the program.

## Setup
- Make sure you have Python 3 installed on your system
- Clone or download the repository

## Usage
- Create an instance of the class SoupProgram and add rules to it
- Create an instance of the class SoupSemantics and pass the program to it
- Create an instance of the class Str2Tr and pass the semantics to it
- Create an instance of the class Config1 and pass the initial configuration to the program
- Use the method roots() and next() of the class Str2Tr to explore the transition relation.


