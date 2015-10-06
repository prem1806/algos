l = [76, 92.3, 'hello', True, 4, 76]
l.append("hello")
l.append(76)
l.insert(3,"cat")
l.insert(0,96)
print l.index("hello")
print l.count(76)
l.pop(l.index(True))
print l