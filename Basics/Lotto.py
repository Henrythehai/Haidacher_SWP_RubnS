import random

def lottoziehung():
    zahlen = list(range(1, 47))
    gezogen = []

    for i in range(6):
        x = random.randrange(46 - i)
        gezogen.append(zahlen[x])

        zahl = zahlen.pop(x)
        zahlen.append(zahl)
    return gezogen

print(lottoziehung())

haufigkeit = [0] * 46

for i in range(1000):
    gezogen = lottoziehung()

    for zahl in gezogen:
        haufigkeit[zahl - 1] += 1

for i in range(1, 47):
    print(i, ":", haufigkeit[i -1])