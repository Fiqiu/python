# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        nextvalue=util.Counter()
        for iteration in range(self.iterations):
            for state in self.mdp.getStates():
                action=self.computeActionFromValues(state)
                nextvalue[state]=self.computeQValueFromValues(state,action)
            self.values=nextvalue.copy()
        
    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        AftertakeAction=[]
        if action==None:
                return 0
        else:
            for nextstate,transprob in self.mdp.getTransitionStatesAndProbs(state, action):
                AftertakeAction.append(transprob*(self.mdp.getReward(state, action, nextstate)+self.discount*self.values[nextstate]))
        return sum(AftertakeAction)
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        if self.mdp.isTerminal(state):
            return None
        else:
            allQvalueAndAction=[]
            allQvalue=[]
            for action in self.mdp.getPossibleActions(state):
                qvalue=self.computeQValueFromValues(state,action)
                allQvalue.append(qvalue)
                allQvalueAndAction.append((action,qvalue))
            for action,Qvalue in allQvalueAndAction:
                if Qvalue==max(allQvalue):
                    return action
            
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        for iteration in range(self.iterations):
            states=self.mdp.getStates()
            num=iteration%len(states)
            action=self.computeActionFromValues(states[num])
            self.values[states[num]]=self.computeQValueFromValues(states[num],action)

class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)
        
    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        
        predecessors={}
        for state in self.mdp.getStates():
            for action in self.mdp.getPossibleActions(state):
                for stat,prob in self.mdp.getTransitionStatesAndProbs(state,action):
                    if stat in predecessors.keys() and prob != 0:
                        predecessors[stat].add(state)
                    else:
                        predecessors[stat]=set()
                        predecessors[stat].add(state)
        def diffs(state):
            maxq=self.computeQValueFromValues(state,self.computeActionFromValues(state))
            diff=abs(self.values[state]-maxq)
            return diff
        
        pq=util.PriorityQueue()
        for state in self.mdp.getStates():
            if not self.mdp.isTerminal(state):
                diff=diffs(state)
                pq.push(state,-diff)
        for iteration in range(self.iterations):            
            if not pq.isEmpty():
                s = pq.pop()
                if not self.mdp.isTerminal(s):                    
                    allQvalue=[]
                    for action in self.mdp.getPossibleActions(s):
                        qvalue=self.computeQValueFromValues(s,action)
                        allQvalue.append(qvalue)
                    self.values[s]=max(allQvalue)
                    for p in predecessors[s]:
                            if not self.mdp.isTerminal(p):
                                diff=diffs(p)
                                if diff>self.theta:
                                    pq.update(p,-diff)
