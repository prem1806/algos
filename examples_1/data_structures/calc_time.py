import time
n = int(raw_input())
start = time.time()
sum = 0
for i in range(0, n):
    sum = sum + i
end = time.time()
print str(end - start) + " seconds"
