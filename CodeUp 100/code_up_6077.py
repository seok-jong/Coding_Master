#
# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
#
# 예시
# #다음 코드는 홀 수만 더해 출력한다.
# n = int(input())
# s = 0
# for i in range(1, n+1) :
#   if i%2==1 :
#     s += i
#
# print(s)

#code

a=int(input())
tmp=0
for i in range(a+1):
    if i%2==0:
        tmp+=i

print(tmp)
