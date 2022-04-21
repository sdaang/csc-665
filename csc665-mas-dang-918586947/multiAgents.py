# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # Initialization
        totalScore = successorGameState.getScore()
        shortestPelletDis = 10000  # set to a large number that can be used as comparison

        # Check if game has been won or not
        if (successorGameState.isWin()):
            return float("inf") - 20

        # Check if pacman is stopped or not
        if (action == Directions.STOP):
            totalScore -= 1000

        # Find the shortest distance for each food pellet
        for foodPellet in newFood.asList():
            # Call manhattanDistance function to find the distance between pacman and the pellet
            pelletDistance = manhattanDistance(foodPellet, newPos)

            # If the new pellet distance is shorter replace the shortest pellet distance value
            if (shortestPelletDis > pelletDistance):
                shortestPelletDis = pelletDistance

        # PACMAN EATS PELLET -> ADDS TO SCORE
        if (currentGameState.getNumFood() > successorGameState.getNumFood()):
            totalScore += 100

        totalScore -= 3 * shortestPelletDis

        return totalScore


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        return self.miniMax(gameState, self.depth)[1]

    def miniMax(self, State, depth, index=0):
        """Code should expand game tree to an arbitrary depth."""
        # Need to grab agents
        agents = State.getNumAgents()
        ghostAgents = State.getNumAgents() - 1
        actionArray = []
        legalActions = State.getLegalActions(index)
        newIndex = (1 + index) % agents

        # Need to check all game states! Need all three conditions ->
        # If game has been either won or lost return.
        # If depth has reached 0 return.
        if depth == 0 or State.isWin() or State.isLose():
            return (self.evaluationFunction(State),)  # return current score

        if (index == ghostAgents):
            aDepth = depth - 1
        elif (index != ghostAgents):
            aDepth = depth

        # append legal game actions into the action array
        for gameAction in legalActions:
            actionArray.append(
                (self.miniMax(State.generateSuccessor(index, gameAction), aDepth, newIndex)[0], gameAction))

        # if the index is not 0, call the min() function to store into action
        if index != 0:
            action = min(actionArray)
        else:
            action = max(actionArray)  # else call on the max() function to store into action

        return action


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def minimumVal(self, state, index, depth, x, y):

        # Variable Initialization
        depthF = 1 + depth
        depthMod = depthF % self.number_of_agents
        value = (float("inf"), "Stop")

        # iterate through all the legal actions
        for action in state.getLegalActions(index):
            value = min([value, (self.value(state.generateSuccessor(index, action), depthMod, depthF, x, y), action)],
                        key = lambda index: index[0])

            # if the value is bigger than a exit, if not return the value
            if (x < value[0]):
                exit;
            elif (x > value[0]):
                return value

            y = min(y, value[0])
        return value

    def maxvalue(self, state, index, depth, x, y):

        # Variable Initialization
        depthF = 1 + depth
        depthMod = depthF % self.number_of_agents
        value = (float("-inf"), "Stop")

        for action in state.getLegalActions(index):
            value = max([value, (self.value(state.generateSuccessor(index, action), depthMod, depthF, x, y), action)],
                        key=lambda index: index[0])

            # if the value is less than b exit, else return the value
            if (y > value[0]):
                exit;
            elif (y < value[0]):
                return value

            x = max(x, value[0])
        return value

    def value(self, state, aIndex, currentdepth, a, b):
        if state.isLose() or state.isWin() or currentdepth >= self.depth * self.number_of_agents:
            return self.evaluationFunction(state)
        retVal = (self.maxvalue(state, aIndex, currentdepth, a, b)[0]) if (aIndex == 0) else (
            self.minimumVal(state, aIndex, currentdepth, a, b)[0])
        return retVal

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        self.number_of_agents = gameState.getNumAgents()
        x = float("-inf")
        y = float("inf")
        return self.maxvalue(gameState, 0, 0, x, y)[1]


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        return self.expectiMax(gameState, self.depth, 0)[1]

    def expectiMax(self, State, depth, index=0):
        """ takes in arguments:
            State - the current game state
            depth - depth of current game state
            index - index of the agent """
        # Initializations
        agents = State.getNumAgents()
        ghostAgents = State.getNumAgents() - 1
        legalActions = State.getLegalActions(index)
        actions = State.getLegalActions(index)
        newIndex = (index + 1) % agents
        actionArray = []

        # Need to check all game states! Need all three conditions ->
        # If game has been either won or lost return.
        # If depth has reached 0 return.
        if depth == 0 or State.isWin() or State.isLose():
            return (self.evaluationFunction(State),)  # return score

        if (index != 0):
            alphaM = 0
        elif (index == 0):
            alphaM = -100000

        if (index == ghostAgents):
            depth = depth - 1

        for gameAction in legalActions:
            # Successor state is passed to the min node and store data into actionResult
            actionResult = (self.expectiMax(State.generateSuccessor(index, gameAction), depth, newIndex))
            # if not the root execute the following
            if index != 0:
                maxAction = gameAction
                alphaM = alphaM + 1.0 / len(actions) * actionResult[0]
            elif (index == 0):
                if alphaM < actionResult[0]:
                    maxAction = gameAction
                    alphaM = actionResult[0]

        return alphaM, maxAction


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newFoodList = newFood.asList()
    min_food_distance = -1
    for food in newFoodList:
        distance = util.manhattanDistance(newPos, food)
        if min_food_distance >= distance or min_food_distance == -1:
            min_food_distance = distance

    distances_to_ghosts = 1
    proximity_to_ghosts = 0
    for ghost_state in currentGameState.getGhostPositions():
        distance = util.manhattanDistance(newPos, ghost_state)
        distances_to_ghosts += distance
        if distance <= 1:
            proximity_to_ghosts += 1

    """Obtaining the number of capsules available"""
    newCapsule = currentGameState.getCapsules()
    numberOfCapsules = len(newCapsule)

    """Combination of the above calculated metrics."""
    return currentGameState.getScore() + (1 / float(min_food_distance)) - (
            1 / float(distances_to_ghosts)) - proximity_to_ghosts - numberOfCapsules


# Abbreviation
better = betterEvaluationFunction
