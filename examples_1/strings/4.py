"""no digits in given number"""

def findNumDigits(n):
    n1 = str(n)
    return len(n1)

n = int(raw_input())
print findNumDigits(n)