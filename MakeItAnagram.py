

w1 = raw_input()
w2 = raw_input()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    c1=w1.count(letter)
    c2=w2.count(letter)
    #print letter
    #print c1
    #print c2
    if c1>c2:
        w1=w1.replace(letter,'',c1-c2)
        total += 1
    if c2>c1:
        w2=w2.replace(letter,'',c2-c1)
        total += 1
    #print w1
    #print w2
 

#print w1
#print w2
print total
