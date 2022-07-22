#1113
X,Y = map(int,input().split())
while(X != Y):
    if(X > Y):
        print('Decrescente')
        X,Y = map(int,input().split())
    elif(X < Y):
        print('Crescente')
        X,Y = map(int,input().split())
