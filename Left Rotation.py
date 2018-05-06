nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))
for i in range(0,d):
    t = a[0]
    a.remove(a[0])
    a.append(t)
print(" ".join(str(x) for x in a))
