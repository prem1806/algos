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