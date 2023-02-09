# IProxy

This repository contains the source code for three proxy classes: IdentityProxy, ParentTraceProxy and ReplaceRootsProxy.

## Purpose
This repository is intended to be used as a tool for exploring and manipulating graphs.

## Contents
- I_Proxy.py: This file contains the code for the IdentityProxy class, which is used as a base class for the other two proxy classes. It allows to get the attributes of the operand passed to the class.

- P_T_Proxy.py: This file contains the code for the ParentTraceProxy class, which is a subclass of IdentityProxy. It allows to explore a graph and keep a trace of the parent of each visited node by using a dictionary. It contains two methods:
    - roots(): it returns the roots of the graph and adds them to the dictionary.
    - next(source): it returns the neighbours of the source node and adds them to the dictionary if they don't have a parent yet.

- R_R_Proxy.py: This file contains the code for the ReplaceRootsProxy class, which is a subclass of IdentityProxy. It allows to change the roots of a graph. It contains one method:
    - roots(): it returns the new roots passed as parameter in the constructor.

- getTrace(dict, target): This function takes a dictionary and a target node as input and returns a list of nodes that is the path from the target to the root of the graph

## Setup
- Make sure you have Python 3 installed on your system
- Clone or download the repository

## Usage
- Use IdentityProxy as a base class for other proxies
- Use ParentTraceProxy to explore a graph and keep a trace of the parent of each visited node
- Use ReplaceRootsProxy to change the roots of a graph
- Use getTrace(dict, target) to get the path from a target node to the root
