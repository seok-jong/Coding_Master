
d=[[0]*19 for _ in range(19)]

n = int(input())

for i in range(n):
    a,b=list(map(int,input().split()))
    d[a-1][b-1]=1


for i in range(19):
    for j in range(19):
        print(d[i][j],end=' ')
        if j==18 and i!=18:
            print()
