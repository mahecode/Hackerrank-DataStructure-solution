n = int(input())
strings = []
for i in range(0,n):
    s = str(input())
    strings.append(s)
q = int(input())
for i in range(0,q):
    cstring = str(input())
    print(strings.count(cstring))
