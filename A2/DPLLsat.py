#!/usr/bin/python3
# CMPT310 A2
#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 45
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
The assignments take far too much time and are very difficult. The class material is
okay compared to them. I would advise to shorten them because they simply take up
too much time and people need to focus on other classes as well.

"""
#####################################################
#####################################################
import sys, getopt
import copy
import random
import time
import numpy as np
sys.setrecursionlimit(10000)

class SatInstance:
    def __init__(self):
        pass

    def from_file(self, inputfile):
        self.clauses = list()
        self.VARS = set()
        self.p = 0
        self.cnf = 0
        with open(inputfile, "r") as input_file:
            self.clauses.append(list())
            maxvar = 0
            for line in input_file:
                tokens = line.split()
                if len(tokens) != 0 and tokens[0] not in ("p", "c"):
                    for tok in tokens:
                        lit = int(tok)
                        maxvar = max(maxvar, abs(lit))
                        if lit == 0:
                            self.clauses.append(list())
                        else:
                            self.clauses[-1].append(lit)
                if tokens[0] == "p":
                    self.p = int(tokens[2])
                    self.cnf = int(tokens[3])
            assert len(self.clauses[-1]) == 0
            self.clauses.pop()
            if (maxvar > self.p):###############################
                print("Non-standard CNF encoding!")
                sys.exit(5)
        # Variables are numbered from 1 to p
        for i in range(1, self.p + 1):
            self.VARS.add(i)

    def __str__(self):
        s = ""
        for clause in self.clauses:
            s += str(clause)
            s += "\n"
        return s


def main(argv):
    inputfile = ''
    verbosity = False
    inputflag = False
    try:
        opts, args = getopt.getopt(argv, "hi:v", ["ifile="])
    except getopt.GetoptError:
        print('DPLLsat.py -i <inputCNFfile> [-v] ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('DPLLsat.py -i <inputCNFfile> [-v]')
            sys.exit()
        ##-v sets the verbosity of informational output
        ## (set to true for output veriable assignments, defaults to false)
        elif opt == '-v':
            verbosity = True
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            inputflag = True
    if inputflag:
        instance = SatInstance()
        instance.from_file(inputfile)
        #start_time = time.time()
        solve_dpll(instance, verbosity)
        #print("--- %s seconds ---" % (time.time() - start_time))

    else:
        print("You must have an input file!")
        print('DPLLsat.py -i <inputCNFfile> [-v]')


# Finds a satisfying assignment to a SAT instance,
# using the DPLL algorithm.
# Input: a SAT instance and verbosity flag
# Output: print "UNSAT" or
#    "SAT"
#    list of true literals (if verbosity == True)
#
#  You will need to define your own
#  DPLLsat(), DPLL(), pure-elim(), propagate-units(), and
#  any other auxiliary functions

def solve_dpll(instance, verbosity):
    #print(instance)
    # instance.VARS goes 1 to N in a dict
    #print(instance.VARS)
    #print(verbosity)
    ###########################################
    # Start your code
    clauses = instance.clauses
    res = DPLL([], clauses)
    
    if res:
        print("SAT")
        if verbosity:
            trueLits = []
            for var in res:
                if var > 0:
                    trueLits.append(var)
            trueLits.sort()
            print(trueLits)
    else:
        print("UNSAT")

    return True

def UnitPropagation(clauses):
    unitList = []
    unitClauses = [clause for clause in clauses if len(clause) == 1] 
    while len(unitClauses) >= 1: 
        unit = unitClauses[0]
        clauses = EliminateClause(clauses, unit[0]) 
        unitList += [unit[0]]
        if clauses == -1:
            return -1, []
        if not clauses:
            return clauses, unitList
        unitClauses = [clause for clause in clauses if len(clause) == 1]
    return clauses, unitList

def PureElimination(clauses):
    pureList = []
    pureLits = []
    occ = NumOccurences(clauses)
    for i, j in occ.items():
        if -i not in occ: pureLits.append(i) 
    for pure in pureLits:
        clauses = EliminateClause(clauses, pure) 
    pureList += pureLits
    return clauses, pureList

def DPLL(varlist, clauses):
    clauses, pureLits = PureElimination(clauses) 
    clauses, unitClauses = UnitPropagation(clauses)

    varlist += (unitClauses + pureLits)
    if clauses == -1:
        return []
    if not clauses:
        return varlist
    
    occ = NumOccurences(clauses)
    counterlist = []
    for key in occ:
        counterlist.append(key)
    P = random.choice(counterlist)

    ret = DPLL(varlist+[P], EliminateClause(clauses, P))
    if not ret:
        ret = DPLL(varlist+[-P], EliminateClause(clauses, -P))
    return ret
    
def EliminateClause(clauses, P):
    newclauses = []
    for clause in clauses:
        if P in clause: 
            continue 
        if -P in clause:
            unit = []
            for literal in clause:
                if literal != -P:
                    unit.append(literal)
            if len(unit) == 0: 
                return -1
            newclauses.append(unit)
        else:
            newclauses.append(clause)
    return newclauses

def NumOccurences(clauses): 
    occurences = {}
    for clause in clauses:
        for literal in clause:
            if literal in occurences:
                occurences[literal] += 1
            else:
                occurences[literal] = 1
    return occurences

    ###########################################


if __name__ == "__main__":
   main(sys.argv[1:])
