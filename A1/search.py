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

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 35
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>
The most interesting is when Max talks about AI in the real world. That stuff is cool.
I had some trouble understanding how to implement A* search and it took a while
to understand what was going on in the code initially when I started question 1.
It's a lot to take in. In class I'm often left confused about the search algorithms
we discuss and I later have to go back and read the slides and watch videos to fully
understand what is going on. I think if Max spends more time explaning the algorithm
itself, it would help a lot of students understand better. Some tricky concepts are
involved with some of these algorithms and more time should be spent on these concepts
and perhaps less time on the analysis of time and space complexity.

"""
#####################################################
#####################################################

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

def depthFirstSearch(problem):
    """
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    
    print ( problem.getStartState() )
    
    You will get (5,5)
    
    print (problem.isGoalState(problem.getStartState()) )
    
    You will get True

    print ( problem.getSuccessors(problem.getStartState()) )
    
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
    # fringe = util.Stack()
    # pathfringe = util.Stack()
    # visited = []
    # path = []
    # fringe.push(problem.getStartState())
    # pathfringe.push(problem.getStartState())
    # i=0

    # while not fringe.isEmpty():

    #     node=fringe.pop()          #tracks states
    #     actionNode=pathfringe.pop()  #tracks actions
    #     #print(node)
    #     if i>0:
    #         path.append(actionNode)

    #     if problem.isGoalState(node): #goal found
    #         while "a" in path:
    #             path.remove("a")
    #         return path

    #     if node not in visited:      #mark as visited
    #         visited.append(node)

    #     if len(problem.getSuccessors(node))>=3 or (node==problem.getStartState() 
    #     and len(problem.getSuccessors(node))>=2): #if 2 or more path options
    #         path.append("a")
    #         if(len(problem.getSuccessors(node)))>=4 or (node==problem.getStartState() 
    #         and len(problem.getSuccessors(node))>=3): #if 3 or more path options
    #             path.append("a")

    #     deadEnd = True
    #     for successor in problem.getSuccessors(node):
    #         if successor[0] not in visited:
    #             deadEnd = False
    #             fringe.push(successor[0])
    #             pathfringe.push(successor[1])

    #     if deadEnd == True:
    #         path_len = len(path)-1      #dead end reached, backtrack
    #         while(path[path_len])!="a":
    #             path.pop()
    #             path_len = path_len-1
    #         path.pop()

    #     i=i+1
    visited = []
    fringe = util.Stack()
    fringe.push((problem.getStartState(), []))

    while not fringe.isEmpty():

        (state, path) = fringe.pop() # state = state, path = action list

        if problem.isGoalState(state):  # if goal found
            return path

        if state not in visited:  # add to visited
            visited.append(state)

            for successor in problem.getSuccessors(state): # add each successor to fringe
                if successor not in visited:
                    fringe.push((successor[0], path + [successor[1]]))
                            # path backtracks with state if dead end

def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    visited = []
    fringe = util.Queue()
    fringe.push((problem.getStartState(), []))

    while not fringe.isEmpty():

        (state, path) = fringe.pop() # state = state, path = action list

        if problem.isGoalState(state):  # if goal found
            return path

        if state not in visited:  # add to visited
            visited.append(state)

            for successor in problem.getSuccessors(state): # add each successor to fringe
                if successor not in visited:
                    fringe.push((successor[0], path + [successor[1]]))
                            # path backtracks with state if dead end

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
    visited = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0 ), 0)

    while not fringe.isEmpty():
        node = fringe.pop()

        if problem.isGoalState(node[0]):
            return node[1]      #goal found

        if node[0] not in visited:
            visited.append(node[0])     #add visited nodes
        else:
            continue        #if node has been visited, continue and get next
                            #node from pqueue
        for successor in problem.getSuccessors(node[0]): #loop through successors
            if successor[0] not in visited:
                cost = heuristic(successor[0], problem)
                fringe.update((successor[0], node[1] + [successor[1]], node[2] + successor[2]), (cost + successor[2] + node[2]))
                    #keep track of state, path, cost to get to node, and cost to node + goal (priority)
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
