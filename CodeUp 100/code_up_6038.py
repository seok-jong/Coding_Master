#
# 정수 2개(a, b)를 입력받아
# a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
#
# 예시
# ...
# c = int(a)**int(b)
# print(c)


#code

a,b = list(map(int,input().split()))

print(a**b)