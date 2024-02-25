# Smart Pacman: Implementing Search Functionality

## Demo
![Demo](./pacmanDemo1.gif)


## Overview
In this project, I have created a basic Pacman AI using different search algorithms (DFS, BFS, Dijkstra’s, A-star) to enable Pacman to intelligently reach a defined goal state (Ex: eating all the food on the map).  

To implement A-star, I developed heuristics to estimate the cost for Pacman to reach the goal state given its current state.

For example: The Manhattan Distance heuristic: ( `abs(start X pos - goal X pos) + abs(start Y pos - goal Y pos)` ) to estimate the cost to move from `[start X, start Y]` to `[goal X, goal Y]`

## The most relevant code can be found in:

### ` search.py`
- Line 75: `def depthFirstSearch(problem: SearchProblem)`
- Line 102: `def breadthFirstSearch(problem: SearchProblem)`
- Line 130: `def uniformCostSearch(problem: SearchProblem)`
- Line 164: `def aStarSearch(problem: SearchProblem, heuristic)`

### `searchAgents.py`
- Line 376: `class FoodSearchProblem`
- Line 432: `def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem)`