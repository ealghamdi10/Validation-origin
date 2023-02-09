from collections import deque # import the deque class from collections module
from graph import Graph # import the Graph class from the graph module
from bfs import * # import all functions from the bfs module
from Hanoi import * # import all functions from the Hanoi module
from HanoiConfiguration import * # import all functions from the HanoiConfiguration module
from termcolor import colored # import the colored function from the termcolor module

 # create an instance of the Graph class with vertex "a" as the starting point
g1 = Graph({
    "a": ["b", "c"],
    "b": ["e", "f"],
    "c": [],
    "d": ["d", "f"],
    "e": ["d"],
    "f": ["f"]
}, "a")

# create another instance of the Graph class with vertex "x" as the starting point
g2 = Graph({
    "x": ["y", "a"],
    "y": ["z"],
    "z": ["x"],
    "a": ["a", "b"],
    "b": ["y", "c"],
    "c": []
}, "x")

# create a dictionary representing a graph

graph1 = {
    "a": ["b", "c"],
    "b": ["e", "f"],
    "c": [],
    "d": ["d", "f"],
    "e": ["d"],
    "f": ["f"]
}

# function to be called when entering a vertex
def on_entry(source, n, acc):
    if n is acc : # check if the current vertex is the target
        print(colored(f"{n} is the target", 'green')) # print target in green
    else :
        print(colored(f"{n} is not the target", 'red')) # print not the target in red

# function to be called when exiting a vertex
def on_exit(source, n, acc):
    if n is acc :
        print("target %s" % n) # print target if the current vertex is the target
    else :
        print("known %s" % n) # print known if the current vertex is not the target

# function to be called when visiting a known vertex
def on_known(source, n, acc):
    if n is acc :
        print("target %s" % n) # print target if the current vertex is the target
    else :
        print("known %s" % n) # print known if the current vertex is not the target

# function to be called when visiting a known vertex
def on_known(source, acc):
    pass # do nothing


# call the bfs_with_accepting function with the graph, target vertex, and the three callbacks
print(bfs_with_accepting(g1, "f", on_entry, on_entry, on_known))


'''
This code is doing the following:

1 - It imports the necessary modules, classes and functions.
2 - It creates two instances of the Graph class, one with vertex "a" as the starting point and another with vertex "x" as the starting point.
3 - It defines 4 functions that will be called at different stages of BFS traversal
4 - It calls the bfs_with_accepting function, passing the graph instance, target vertex, and the three callback functions as arguments.
5 - This bfs_with_accepting function performs the Breadth-First Search algorithm on the graph instance, starting from the given vertex,
    using the provided callback functions to handle certain events during the traversal. 
    It will call the on_entry function when entering a vertex, the on_exit function when exiting a vertex, 
    and the on_known function when visiting a known vertex. 
    It will also check if the current vertex is the target vertex and print the appropriate message based on the result.
'''
