n1 = int(input())
n2 = int(input())
n3 = int(input())
minnn = min(n1, n2, n3)
maxxx = max(n1, n2, n3)
summm = sum([n1, n2, n3])
sred = summm - minnn - maxxx
print((minnn * sred) * maxxx)
