a = int(raw_input("Enter a number to check if it is happy: "))
visited = set()
while 1:
    if a == 1:
        print "Number is happy!"
        break
    a = sum(int(c) ** 2 for c in str(a))
    print a
    if a in visited:
        print "Number is sad!"
        break
    visited.add(a)
