class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
   
    def enqueue(self, item):
        self.items.insert(0,item)
  
    def dequeue(self):
        return self.items.pop()
  
    def size(self):
        return len(self.items)
   
       
  
q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print q.items


#queue two stack...
class Queue(object):
    def __init__(self):
        self.instack = []
        self.outstack = []
     
    def enqueue(self,element):
        self.instack.append(element)
    
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()    

q = Queue()
for i in xrange(5):
    q.enqueue(i)
for i in xrange(5):
    print q.dequeue()



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


#permitaion....
def permutate(seq):
    if not seq:
        return [seq]  
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            print k, part  # test
            for m in permutate(part):
                print m
                temp.append(seq[k:k+1] + m)
                print temp
                #print m, seq[k:k+1], temp  # test
        #print temp
        return temp





permutate('pre')





#satck...

class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


from stack import Stack

s=Stack()

s.push(100)
print s.items
s.pop()
print s.items
s.push(1),s.push(2),s.push(3),s.push(4),s.push(5),s.push(6)
print s.items
print(s.isEmpty())
print s.peek()
print s.size()
s.push(")))))))))))))goodbad")
s.push(')')
print s.items
