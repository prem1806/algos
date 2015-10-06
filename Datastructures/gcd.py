def gcd(a, b):
    while b != 0:
        (a, b) = (b, a%b)
    return a
a,b = raw_input().split()
a,b = int(a),int(b)
print gcd(a,b)
