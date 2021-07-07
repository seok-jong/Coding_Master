#
# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10
#
# 예시
# a = 2
# b = 10
# print(a << b)  #2^10 = 1024 가 출력된다.

#code

a,b = list(map(int,input().split()))

print(a<<b)
