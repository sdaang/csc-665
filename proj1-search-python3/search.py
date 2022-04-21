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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # Initialization of STACK for tuple obj
    searchStack, visited = util.Stack(), set()
    searchStack.push((problem.getStartState(), []))  # push onto the stack

    # While the stack isn't empty we need to keep track of visited nodes and push it and if it reaches
    # the goal state we need to break out of the code block and return
    while (not searchStack.isEmpty()):
        # while the stack isn't empty grab node at top of stack
        currentNodeState, direction = searchStack.pop()

        # if goal state is reached, break out of block
        if (problem.isGoalState(currentNodeState) == True):
            break
        elif (problem.isGoalState(currentNodeState) == False):
            # First issue - added visited in the actual for loop and had it crash. It was adding every time it went
            # through that for loop which wasn't good. Better to check if the current node has been visited
            # outside of the for loop lol
            if currentNodeState not in visited:
                visited.add(currentNodeState)

                # NOTE - COST NOT NEEDED FOR DFS, only use state and direction on the list
                for element in problem.getSuccessors(currentNodeState):
                    # assign tup values into variables to be used
                    newNodeDirection = element[1]
                    newNodeState = element[0]

                    # rewrite the new path using the value from the tup and the current node direction as well
                    newPath = direction + [newNodeDirection]
                    searchStack.push((newNodeState, newPath))

    return direction


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    # Initialization
    searchQueue, visited = util.Queue(), set()
    # This time we need to keep track of cost so we need that third item to be pushed onto the queue
    searchQueue.push((problem.getStartState(), [], 0))

    while (not searchQueue.isEmpty()):
        # while the stack isn't empty retrieve items in queue using pop operation
        currentNodeState, direction, pathCost = searchQueue.pop()

        # If goal state is reached, break out of block and return
        if (problem.isGoalState(currentNodeState) == True):
            break
        # if the goal state has not been reached yet execute the following
        elif (problem.isGoalState(currentNodeState) == False):
            # Need to check if node is in visited or not first
            if currentNodeState not in visited:
                visited.add(currentNodeState)  # if not visited add to the visited list
                for element in problem.getSuccessors(currentNodeState):
                    # Store tup values into new variables
                    newNodeState = element[0]
                    newNodeDirection = element[1]
                    newPathCost = element[2]

                    newCost = pathCost
                    newCost += newPathCost  # calculate the new path cost
                    newDirection = direction + [newNodeDirection]  # calculate new direction

                    # Push the new node state, direction, and path cost
                    searchQueue.push((newNodeState, newDirection, newCost))

    return direction


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # NOTE: visited cannot = [] since list indices must be int or slices, not tuples
    # so visited = {}
    searchPriorityQueue, visited = util.PriorityQueue(), {}
    searchPriorityQueue.push((problem.getStartState(), [], 0), 0)

    while (not searchPriorityQueue.isEmpty()):
        # pop the current node in the priority queue
        currentNodeState, direction, pathCost = searchPriorityQueue.pop()

        # Again, if goal state is reached break out of block
        if (problem.isGoalState(currentNodeState) == True):
            break
            # If goal state not reached, execute below
        elif(problem.isGoalState(currentNodeState) == False):
            # Check if visited, if not check to see if the new path cost is less than what's been visited
            if (currentNodeState not in visited) or (visited[currentNodeState] > pathCost):
                # update the path cost
                updatedCost = pathCost
                # store the new updated lower cost into visited
                visited[currentNodeState] = updatedCost

                for element in problem.getSuccessors(currentNodeState):
                    # Store tuple vals into new variables to be used
                    newNodeState = element[0]
                    newNodeDirection = element[1]
                    newPathCost = element[2]

                    newCost = pathCost
                    newCost += newPathCost  # new cost will be the original pathcost + the new path cost
                    newDirection = direction + [newNodeDirection]

                    # NOTE: we push our new values onto searchPriorityQueue
                    searchPriorityQueue.push((newNodeState, newDirection, newCost), newCost)
    return direction


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # NOTE: A* is like Dijkstra's Algo, but with heuristic involved
    # Initialization
    searchPriorityQueue, visited = util.PriorityQueue(), set()
    searchPriorityQueue.push((problem.getStartState(), [], 0), 0)

    # Check if the priority queue is empty or not
    while (not searchPriorityQueue.isEmpty()):
        # pop the first node in the queue
        currentNodeState, direction, currentCost = searchPriorityQueue.pop()

        # put the state and cost of the node into visited to be compared later
        visited.add((currentNodeState, currentCost))

        if (problem.isGoalState(currentNodeState) == True):
            break

        elif (problem.isGoalState(currentNodeState) == False):

            # for each successor adjacent to the current node, we want to check if it has been
            # explored or not. If it has not been explored then add it to the explored list. If
            # Need to record all costs. Compare costs and once we find the lowest cost we need
            # to make the newNode with the lowest cost the new currentNode (parent node). Then
            # repeat steps from there. Check if explored, record, compare, change state.
            for element in problem.getSuccessors(currentNodeState):
                newNodeState = element[0]
                newNodeDirection = element[1]
                newPathCost = element[2]

                newPath = direction + [newNodeDirection]
                newNode = (newNodeState, newPath, problem.getCostOfActions(newPath))

                # Check to see if the successor node has been visited or not
                alreadyVisited = False
                for currentNode in visited:
                    currentState, currentCost = currentNode
                    # totalCost = problem.getCostOfActions(newPath) + heuristic(newNodeState, problem)

                    # IMPORTANT COMPARISON -> If both states are the same then ALSO COMPARE COSTS.
                    # If new walkable cost is less than what has already been visited, set alreadyVisited to true
                    # If all has already been visited then keep looping till we get something that hasn't been
                    if (newNodeState == currentState) and (currentCost <= problem.getCostOfActions(newPath)):
                        alreadyVisited = True
                        # print("Node has already been visited")

                # If it has not been visited as of yet, add onto the queue and mark it as visited as well.
                if (not alreadyVisited):
                    # print("Node has not been visited yet, will be added to visited")
                    visited.add((newNodeState, problem.getCostOfActions(newPath)))
                    # push the new nodeState/cost plus the heuristic state/cost
                    searchPriorityQueue.push(newNode, problem.getCostOfActions(newPath) + heuristic(newNodeState, problem))

    return direction


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
