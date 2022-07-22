#1171
n = int(input())
l = []
for i in range(n):
    m = int(input())
    l.append(m)
ls = sorted(set(l))
for i in ls:
    v = l.count(i)
    print('{} aparece {} vez(es)'.format(i, v))