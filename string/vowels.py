text = raw_input("enter the sentance:")
cnt = 0
for x in text:
    if x  in "aeiou":
    	cnt = cnt + 1
print cnt
    