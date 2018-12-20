# logicPlan.py
# ------------
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
In logicPlan.py, you will implement logic planning methods which are called by
Pacman agents (in logicAgents.py).
"""

import util
import sys
import logic
import game


pacman_str = 'P'
ghost_pos_str = 'G'
ghost_east_str = 'GE'
pacman_alive_str = 'PA'

class PlanningProblem:
    """
    This class outlines the structure of a planning problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the planning problem.
        """
        util.raiseNotDefined()

    def getGhostStartStates(self):
        """
        Returns a list containing the start state for each ghost.
        Only used in problems that use ghosts (FoodGhostPlanningProblem)
        """
        util.raiseNotDefined()
        
    def getGoalState(self):
        """
        Returns goal state for problem. Note only defined for problems that have
        a unique goal state such as PositionPlanningProblem
        """
        util.raiseNotDefined()

def tinyMazePlan(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def sentence1():
    """Returns a logic.Expr instance that encodes that the following expressions are all true.
    
    A or B
    (not A) if and only if ((not B) or C)
    (not A) or (not B) or C
    """
    return logic.conjoin([(logic.Expr('A') | logic.Expr('B')) \
            , (~logic.Expr('A') % (~logic.Expr('B')|logic.Expr('C'))) \
            , logic.disjoin([~logic.Expr('A') , ~logic.Expr('B'), logic.Expr('C')])])
    "*** YOUR CODE HERE ***" 
    util.raiseNotDefined()

def sentence2():
    """Returns a logic.Expr instance that encodes that the following expressions are all true.
    
    C if and only if (B or D)
    A implies ((not B) and (not D))
    (not (B and (not C))) implies A
    (not D) implies C
    """
    return logic.conjoin([(logic.Expr('C') % (logic.Expr('B')|logic.Expr('D'))), \
    (logic.Expr('A') >> (~logic.Expr('B')& ~logic.Expr('D'))), \
    (~(logic.Expr('B')&~logic.Expr('C'))>>logic.Expr('A')), \
    (~logic.Expr('D')>>logic.Expr('C'))])
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def sentence3():
    """Using the symbols WumpusAlive[1], WumpusAlive[0], WumpusBorn[0], and WumpusKilled[0],
    created using the logic.PropSymbolExpr constructor, return a logic.PropSymbolExpr
    instance that encodes the following English sentences (in this order):

    The Wumpus is alive at time 1 if and only if the Wumpus was alive at time 0 and it was
    not killed at time 0 or it was not alive and time 0 and it was born at time 0.

    The Wumpus cannot both be alive at time 0 and be born at time 0.

    The Wumpus is born at time 0.
    """
    A=logic.PropSymbolExpr('WumpusAlive',0)
    B=logic.PropSymbolExpr('WumpusAlive',1)
    C=logic.PropSymbolExpr('WumpusBorn',0)
    D=logic.PropSymbolExpr('WumpusKilled',0)
    return logic.conjoin([(B % ((A&~D) | (~A&C))), \
    ~(A&C), \
    C])
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def findModel(sentence):
    """Given a propositional logic sentence (i.e. a logic.Expr instance), returns a satisfying
    model if one exists. Otherwise, returns False.
    """
    "*** YOUR CODE HERE ***"
    return logic.pycoSAT(logic.to_cnf(sentence))
    util.raiseNotDefined()

def atLeastOne(literals) :
    """
    Given a list of logic.Expr literals (i.e. in the form A or ~A), return a single 
    logic.Expr instance in CNF (conjunctive normal form) that represents the logic 
    that at least one of the literals in the list is true.
    >>> A = logic.PropSymbolExpr('A');
    >>> B = logic.PropSymbolExpr('B');
    >>> symbols = [A, B]
    >>> atleast1 = atLeastOne(symbols)
    >>> model1 = {A:False, B:False}
    >>> print logic.pl_true(atleast1,model1)
    False
    >>> model2 = {A:False, B:True}
    >>> print logic.pl_true(atleast1,model2)
    True
    >>> model3 = {A:True, B:True}
    >>> print logic.pl_true(atleast1,model2)
    True
    """
    return logic.conjoin([logic.disjoin(literals),logic.disjoin(literals)])
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def atMostOne(literals) :
    """
    Given a list of logic.Expr literals, return a single logic.Expr instance in 
    CNF (conjunctive normal form) that represents the logic that at most one of 
    the expressions in the list is true.
    """
    "*** YOUR CODE HERE ***"
    cnf=[]
    for i in range(len(literals)):
        if i != literals[-1]:
            for j in literals[i+1:]:
                cnf.append(~literals[i]|~j)
    return logic.conjoin(cnf)
    util.raiseNotDefined()


def exactlyOne(literals) :
    """
    Given a list of logic.Expr literals, return a single logic.Expr instance in 
    CNF (conjunctive normal form)that represents the logic that exactly one of 
    the expressions in the list is true.
    """
    "*** YOUR CODE HERE ***"
    cnf=[]
    for i in range(len(literals)):
        if i != literals[-1]:
            for j in literals[i+1:]:
                cnf.append(~literals[i]|~j)
    def andoperator(x,y):
        return x|y
    cnf.append(reduce(andoperator,literals))
    return logic.conjoin(cnf)
    util.raiseNotDefined()


def extractActionSequence(model, actions):
    """
    Convert a model in to an ordered list of actions.
    model: Propositional logic model stored as a dictionary with keys being
    the symbol strings and values being Boolean: True or False
    Example:
    >>> model = {"North[3]":True, "P[3,4,1]":True, "P[3,3,1]":False,
    "West[1]":True, "GhostScary":True, "West[3]":False, "South[2]":True, "East[1]":False}
    >>> actions = ['North', 'South', 'East', 'West']
    >>> plan = extractActionSequence(model, actions)
    >>> print plan
    ['West', 'South', 'North']
    """
    allaction=[]
    for i in model:
        if model.get(i)==True:
            log=logic.PropSymbolExpr.parseExpr(i)
            if type(log[1])==str and log[0] in actions:
                allaction.append(log)
    def sort(x):
        return int(x[1])
    allaction.sort(key=sort)
    action=[]
    for i in allaction:
        action.append(i[0])
    return action
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def pacmanSuccessorStateAxioms(x, y, t, walls_grid):
    """
    Successor state axiom for state (x,y,t) (from t-1), given the board (as a 
    grid representing the wall locations).
    Current <==> (previous position at time t-1) & (took action to move to x, y)
    """
    wall=walls_grid.asList()
    adjacentp=[(x,y-1),(x-1,y),(x,y+1),(x+1,y)]
    adjacent=[]
    for i in adjacentp:
        if i not in wall:
            adjacent.append(i)
    action=[]
    coordinate=[]
    for i in adjacent:
        if i==(x,y-1):
            coordinate.append(logic.PropSymbolExpr(pacman_str, x, y-1, t-1))
            action.append(logic.PropSymbolExpr('North',t-1))
        if i==(x,y+1):
            coordinate.append(logic.PropSymbolExpr(pacman_str, x, y+1, t-1))
            action.append(logic.PropSymbolExpr('South',t-1))
        if i==(x-1,y):
            coordinate.append(logic.PropSymbolExpr(pacman_str, x-1, y, t-1))
            action.append(logic.PropSymbolExpr('East',t-1))
        if i==(x+1,y):
            coordinate.append(logic.PropSymbolExpr(pacman_str, x+1, y, t-1))
            action.append(logic.PropSymbolExpr('West',t-1))
    logicst=[]
    for i in range(len(adjacent)):
        logicst.append(logic.conjoin(coordinate[i],action[i]))
    B=logic.disjoin(logicst)
    A=logic.PropSymbolExpr(pacman_str, x, y, t) % B
    "*** YOUR CODE HERE ***"
    return A # Replace this with your expression


def positionLogicPlan(problem):
    """
    Given an instance of a PositionPlanningProblem, return a list of actions that lead to the goal.
    Available actions are game.Directions.{NORTH,SOUTH,EAST,WEST}
    Note that STOP is not an available action.
    """
    
    walls = problem.walls
    width, height = problem.getWidth(), problem.getHeight()
    initial=problem.getStartState()
    first=logic.PropSymbolExpr(pacman_str,initial[0],initial[1],0)
    end=problem.getGoalState()
    Tmax=50
    actions=['West','South','East','North']
    allsuccessors=[]
    allaction=[]
    startstates=[]
    '''
    for x in range(1,width+1):
            for y in range(1,height+1):
                if (x,y) not in walls.asList():
                    startstates.append(logic.PropSymbolExpr(pacman_str,x,y,0))
                    '''
    for t in range(1,Tmax):
        for x in range(1,width+1):
            for y in range(1,height+1):
                if (x,y) not in walls.asList():
                    startstates.append(logic.PropSymbolExpr(pacman_str,x,y,0))
        successor=[]
        goal=logic.PropSymbolExpr(pacman_str, end[0], end[1], t)
        for x in range(1,width+1):
            for y in range(1,height+1):
                if (x,y) not in walls.asList():
                    successor.append(pacmanSuccessorStateAxioms(x, y, t, walls))
        onlystart=exactlyOne(startstates)
        successors=logic.conjoin(successor)
        action=[]
        for i in actions:
            action.append(logic.PropSymbolExpr(i,t-1))
        allaction.append(exactlyOne(action))
        allsuccessors.append(successors)
        #end=logic.conjoin(goal,pacmanSuccessorStateAxioms(x, y, t+1, walls))
        isgoal=findModel(logic.conjoin(onlystart,first,goal,logic.conjoin(allsuccessors),logic.conjoin(allaction)))
        #print isgoal
        if isgoal:
            return extractActionSequence(isgoal,actions)
    "*** YOUR CODE HERE ***"


    util.raiseNotDefined()


def foodLogicPlan(problem):
    """
    Given an instance of a FoodPlanningProblem, return a list of actions that help Pacman
    eat all of the food.
    Available actions are game.Directions.{NORTH,SOUTH,EAST,WEST}
    Note that STOP is not an available action.
    """
    walls = problem.walls
    width, height = problem.getWidth(), problem.getHeight()
    pacinitial=problem.getStartState()[0]
    food=problem.getStartState()[1]
    first=logic.PropSymbolExpr(pacman_str,pacinitial[0],pacinitial[1],0)
    foods=food.asList()
    Tmax=50
    actions=['West','South','East','North']
    allsuccessors=[]
    allaction=[]
    startstates=[]
    allfood=[]
    for x in range(1,width+1):
            for y in range(1,height+1):
                if (x,y) not in walls.asList():
                    startstates.append(logic.PropSymbolExpr(pacman_str,x,y,0))
    onlystart=exactlyOne(startstates)
    
    for t in range(1,Tmax):
        allfood=[]
        successor=[]
        for i in foods:
            foodgoal=[]
            #for j in range(t+1):
            foodgoal.append(logic.PropSymbolExpr(pacman_str,i[0],i[1],t))            
            allfood.append(atLeastOne(foodgoal))
        
        for x in range(1,width+1):
            for y in range(1,height+1):
                if (x,y) not in walls.asList():
                    successor.append(pacmanSuccessorStateAxioms(x, y, t, walls))
        successors=logic.conjoin(successor)
        action=[]
        
        for i in actions:
            action.append(logic.PropSymbolExpr(i,t-1))
        allaction.append(exactlyOne(action))
        allsuccessors.append(successors)
        #end=logic.conjoin(goal,pacmanSuccessorStateAxioms(x, y, t+1, walls))
        isgoal=findModel(logic.conjoin(onlystart,first,logic.conjoin(allfood),logic.conjoin(allsuccessors),logic.conjoin(allaction)))
        #print isgoal
        if isgoal:
            return extractActionSequence(isgoal,actions)
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
plp = positionLogicPlan
flp = foodLogicPlan

# Some for the logic module uses pretty deep recursion on long expressions
sys.setrecursionlimit(100000)
    