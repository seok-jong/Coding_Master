#
# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.
#
# 예시
# print(123<456)  #비교 연산자 < 의 계산 결과인 True(참)가 출력된다.
# (123, 456 은 숫자로 작성된 단어이기 때문에 10진수로 인식된다.)


#code

a,b = list(map(int,input().split()))
print(True if a<b else False)
