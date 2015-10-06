s = raw_input()
l = [word for word in s.split(" ")]
print " ".join(sorted(list(set(l))))

