#
# 십자 뒤집기는
# 그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후,
# 다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
# 어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.
#
# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
#
# 예시
# ...
# for i in range(n) :
#   x,y=input().split()
#   for j in range(1, 20) :
#     if d[j][int(y)]==0 :
#       d[j][int(y)]=1
#     else :
#       d[j][int(y)]=0
#
#     if d[int(x)][j]==0 :
#       d[int(x)][j]=1
#     else :
#       d[int(x)][j]=0
# ...


#code
from pprint import pprint

x=[]
for i in range(19):
    a = list(map(int,input().split()))
    x.append(list(map(lambda x: bool(x), a)))


t=int(input())

for i in range(t):
    a1,a2 =list(map(int,input().split()))
    for j in range(19):

        x[j][a2-1]= not x[j][a2-1]

    x[a1-1]=list(map(lambda x:not x,x[a1-1]))

fin=[]
for i in range(19):
    fin.append(list(map(int,x[i])))

pprint(fin)



# 제출 코드

from pprint import pprint

x=[]
for i in range(19):
    a = list(map(int,input().split()))
    x.append(list(map(lambda x: bool(x), a)))


t=int(input())

for i in range(t):
    a1,a2 =list(map(int,input().split()))
    for j in range(19):

        x[j][a2-1]= not x[j][a2-1]

    x[a1-1]=list(map(lambda x:not x,x[a1-1]))

fin=[]
for i in range(19):
    fin.append(list(map(int,x[i])))


for i in range(19):
    for j in range(19):
        if j ==18:
            print(fin[i][j])
        else:
            print(fin[i][j],end=" ")