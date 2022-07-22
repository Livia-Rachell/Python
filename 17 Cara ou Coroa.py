#1329
Rm = []
Rj = []
m = 1
while(m != 0):
    m = int(input())
    if m == 0:
        break
    N = list(map(int,input().split()))
    for item in N:
        if(item == 0):
            Rm.append(item)
        else:
            Rj.append(item)
    Rj = len(Rj)
    Rm = len(Rm)        
    print('Mary won',Rm,'times and John won',Rj,'times')
    Rm = []
    Rj = []