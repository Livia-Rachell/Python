#2456
l = list(map(int,input().split()))
if(l[0] > l[1] > l[2] > l[3] > l[4]):
    print('D')
elif(l[0] < l[1] < l[2] < l[3] < l[4]):
    print('C')
else:
    print('N')
