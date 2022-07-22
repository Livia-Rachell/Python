n = int(input())
lc = []
lr = []
ls = []
fa = 0
for i in range(n):
    q, t = input().split()
    q = int(q)
    if(t == 'C'):
        lc.append(q)
    if(t == 'R'):
        lr.append(q)
    if(t == 'S'):
        ls.append(q)
c = sum(lc)
r = sum(lr)
s = sum(ls)
total = (c + r + s)
cc = (c*100)/total
rr = (r*100)/total
ss = (s*100)/total
print('Total:',total,'cobaias')
print('Total de coelhos:',c)
print('Total de ratos:',r)
print('Total de sapos:',s)
print('Percentual de coelhos: {:.2f} %'.format(cc))
print('Percentual de ratos: {:.2f} %'.format(rr))
print('Percentual de sapos: {:.2f} %'.format(ss))