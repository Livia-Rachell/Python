#2167
V_Motor = int(input())
RPM = list(map(int, input().split()))
Queda = 0
for i in range(1, len(RPM)):
   if (RPM[i] < RPM[i - 1]):
      Queda = RPM.index(RPM[i]) + 1
      break
print(Queda)