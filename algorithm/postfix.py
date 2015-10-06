#postfix...
from stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    print operandStack
    print postfixExpr
    tokenList = postfixExpr.split()
    print tokenList
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            print operand2,
            print operand1,
            result = doMath(token,operand1,operand2)
            print result
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

(postfixEval('7 8 + 3 2 + /'))