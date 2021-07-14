#
# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.
#
# 참고
# s = input()
# print(s[0:2])

#code

s=input()
a=0
for i in range(2,7,2):
    print(s[a:i],end=" ")
    a=i
