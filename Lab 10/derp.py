"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates prefix expressions 
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Scott C Johnson (scj@cs.rit.edu)

Author: Youssef Naguib
File: derp.py
Language: Python3.7
Description: Lab 10 solution
"""

from dataclasses import dataclass

@dataclass
class MathNode:
    """Represents a mathematical operation"""

    left: 'MathNode'
    op: str
    right: 'MathNode'

@dataclass
class LiteralNode:
    """Represents an operand node"""

    val: int

@dataclass
class VariableNode:
    """Represents a variable node"""

    name: str
    
##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """
    parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    Pre: tokens must be a list of integers, variables, or math operations
         which include + - * //
    Post: constructs a tree using tokens list
    Param: tokens is a list
    """
    if tokens == []:
        raise TypeError('Empty List')
    p = tokens.pop(0)
    if p.isdigit():
        return LiteralNode(int(p))
    elif p.isidentifier():
        return VariableNode(p)
    else:
        left = parse(tokens)
        right = parse(tokens)
        if p in ['*','//','+','-']:
            return MathNode(left,p,right)
        else:
            raise TypeError('wrong type')

##############################################################################
# infix
##############################################################################
        
def infix(node):
    """
    infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression.
    Pre: node must be a valid tree with root as a MathNode
    Post: infix expression of tree is returned
    param: node is a tree
    """
    list = []
    def LRV(node):
        if isinstance(node,MathNode) is True:
            list.append('(')
            if isinstance(node.left,MathNode) is True:
                LRV(node.left)
            if isinstance(node.left,VariableNode) is True:
                list.append(node.left.name)
            if isinstance(node.left,LiteralNode) is True:
                list.append(node.left.val)
            list.append(node.op)
            if isinstance(node.right,VariableNode) is True:
                list.append(node.right.name)
            if isinstance(node.right,LiteralNode) is True:
                list.append(node.right.val)
            LRV(node.right)
            list.append(')')
        return list
    LRV(node)
    s = ''
    idx = 0
    l = len(list)
    for chr in list:
        idx += 1
        if chr not in ['*','//','+','-']:
            if idx == l:
                s += str(chr)
            else:
                s += str(chr) + ' '
        else:
            s += str(chr) + ' '
    return s




##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, symTbl):
    """
    evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl
    Post: variables are substituted with their correct values from the symTbl,
          and the infix equation is evaluated and returned.
    param: node is a tree
    param: symTbl is a dictionary containing integer values for specific
           variables.
    """
    eq = infix(node)
    equation = eq.split()
    for value in range(0,len(equation)-1):
        if equation[value] in symTbl:
            replacer = symTbl[equation[value]]
            equation.pop(value)
            equation.insert(value,replacer)
    abc = ''.join(equation)
    return eval(abc)

    
##############################################################################
# main
##############################################################################
                     
def main():
    """
    main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression
    pre: program must be executed
    post: derp interpreter will interact with user, asking for prefix input,
          displaying a table of appropriate values according to chosen file,
          displaying a infix equation and then solving the equation and
          returning the result to user. Program will repeat until user hits
          enter with empty input.
    """
    print("Hello Herp, welcome to Derp v1.0 :)")
    inFile = input("Herp, enter symbol table file: ")
    symTbl = {}
    with open(inFile) as f:
        for line in f:
            x = line.split()
            symTbl[x[0]] = x[1]
    print('Derping the symbol table (variable name => integer value)')
    for value in symTbl.keys():
        print(value,'=>',symTbl[value])
    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break
        tokens = prefixExp.split()
        tree = parse(tokens)
        t1 = infix(tree)
        print("Derping the infix expression:", t1)
        result = evaluate(tree, symTbl)
        print("Derping the evaluation:", result)
    print("Goodbye Herp :(")
    
if __name__ == "__main__":
    main()
