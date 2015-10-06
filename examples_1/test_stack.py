from stack.stack import Stack
from stack.stack import foo


stk = Stack()
stk.push(1)
stk.push(2)
stk.pop()
stk.push(3)
print stk.peek()
print stk.size()


print foo()