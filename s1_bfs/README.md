# Project validation

##### This Directory contains three Python files for implementing a breadth-first search algorithm on a graph data structure.

## The Directory is composed of:

* **`main.py`** is the entry point of the program, which calls the functions in the other two files(bfs.py & graph.py) to perform the breadth-first search.
* **`bfs.py`** contains the implementation of the breadth-first search algorithm.
* **`graph.py`** contains the implementation of the graph data structure and its associated methods.

## Dependencies

This project requires `collections ` and `termcolor ` libraries. To install them, use the following command:

```
pip install termcolor  collections 
```

## Running the program

```
python main.py
```

### Example of the excepted Result

```diff
- b is not the target
- c is not the target
- e is not the target
+ f is the target
- d is not the target
+ f is the target
- d is not the target
+ f is the target
{'e', 'd', 'a', 'f', 'b', 'c'}
```
