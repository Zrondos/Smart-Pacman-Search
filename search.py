# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Performs depth first search to reach problem.goalState

    Returns optimal list of actions to reach goal state
    """
    
    visited = set()
    currentState = problem.getStartState()
    notVisited = util.Stack() #Setting up FIFO notVisited list
    currentPath= [] #List of actions to get to currentState
    notVisited.push((currentState,currentPath ))

    while not notVisited.isEmpty():
        currentState, currentPath = notVisited.pop()
        if problem.isGoalState(currentState): #If goal state reached, return the path to get to this state
            return currentPath 
        if currentState not in visited:
            succesorStates = problem.getSuccessors(currentState) #Generate all sucessor positions, based on legal moves
            for nextState,action, currentCost in succesorStates:
                newPath = currentPath + [action]
                notVisited.push((nextState, newPath)) #Add all successor positions and paths to notVisited list
        visited.add(currentState) #Mark currentState as visited
    pathIfNoSolution = [] #If there is no valid path that results in goal state, no actions can be taken
    return pathIfNoSolution


def breadthFirstSearch(problem: SearchProblem):
    
    """
    Performs breadth first search to reach problem.goalState

    Returns optimal list of actions to reach goal state
    """

    visited = set()
    currentState = problem.getStartState() #Start position of Pacman
    notVisited = util.Queue() #Setting up LIFO notVisited list
    currentPath = [] #List of actions to get to currentState
    notVisited.push((currentState, currentPath))

    while not notVisited.isEmpty():
        currentState, currentPath = notVisited.pop()
        if problem.isGoalState(currentState): #If goal state reached, return the path to get to this state
            return currentPath
        if currentState not in visited:
            successorStates = problem.getSuccessors(currentState) #Generate all sucessor positions, based on legal moves
            for nextState, action, currentCost in successorStates:
                newPath = currentPath + [action] #Adding the action to the path to get to this sucessor state
                notVisited.push( (nextState, newPath)) #Add successor position and path to notVisited list
            visited.add(currentState) #Mark currentState as visited
    pathIfNoSolution = [] 
    return pathIfNoSolution #If there is no valid path that results in goal state, no actions can be taken


def uniformCostSearch(problem: SearchProblem):
    """
    Performs Dijstak's algorithm search where cost between nodes is a constant value
    Returns optimal list of actions to reach goal state

    """
    visited = set()
    currentState = problem.getStartState() #Start position of Pacman
    notVisited = util.PriorityQueue() #Setting up PriorityQueue notVisited list
    currentPath = [] #List of actions to get to currentState
    currentCost = 0 #The cost to get to this state. 1 action increases cost by 1
    notVisited.push( (currentState, currentPath, currentCost), currentCost) 

    while not notVisited.isEmpty():
        currentState, currentPath, currentCost = notVisited.pop()
        if problem.isGoalState(currentState): #If goal state reached, return the path to get to this state
            return currentPath
        if currentState not in visited:
            successorStates = problem.getSuccessors(currentState) #Generate all sucessor positions, based on legal moves
            for nextState, action, actionCost in successorStates:
                newPath = currentPath + [action] #Adding the action to the path to get to this sucessor state
                newCost = currentCost + actionCost #Updating the cost to get to this state
                notVisited.push( (nextState, newPath, newCost), newCost) #Add successor position, path, and cost to notVisited list
            visited.add(currentState) #Mark currentState as visited
    pathIfNoSolution = [] #If there is no valid path that results in goal state, no actions can be taken
    return pathIfNoSolution

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    visited = set()
    notVisited = util.PriorityQueue() #Setting up PriorityQueue notVisited list

    currentState = problem.getStartState() #Start position of Pacman
    currentPath = [] #List of actions to get to currentState
    currentCost = 0 #The cost to get to this state. 1 action increases cost by 1

    notVisited.push((currentState, currentPath, currentCost), currentCost)

    while not notVisited.isEmpty():
        currentState, currentPath, currentCost = notVisited.pop()
        if problem.isGoalState(currentState): #If goal state reached, return the path to get to this state
            return currentPath
        if currentState not in visited:
            successorStates = problem.getSuccessors(currentState) #Generate all sucessor positions, based on legal moves
            for child,action,actionCost in successorStates: 
                newPath = currentPath + [action]  #Adding the action to the path to get to this sucessor state
                newCost = currentCost +  actionCost #Updating the cost to get to this state
                estimatedCostToGoal = newCost + heuristic(child,problem) #Calculate estimated cost to reach goal state based on provided heuristic. Ex: Using Manhattan distance from goal to estimate cost
                notVisited.push( (child, newPath, newCost), estimatedCostToGoal)  #Add successor position, path, and cost to notVisited list
        visited.add(currentState)  #Mark currentState as visited
    pathIfNoSolution = [] #If there is no valid path that results in goal state, no actions can be taken
    return pathIfNoSolution


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
