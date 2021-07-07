#
# 두 정수(a, b)를 입력받아
# a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.
#
# 참고
# 어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용할 수 있다.

#code

a,b =list(map(int,input().split()))

print(True if a==b else False)