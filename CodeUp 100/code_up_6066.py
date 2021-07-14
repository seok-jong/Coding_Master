#
# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
#
# 예시
# ...
# if a%2==0 :
#   print("even")
# else :
#   print("odd")

#code

a,b,c = list(map(int,input().split()))

for i in [a,b,c]:
    if i%2==0:
        print("even")
    else:
        print("odd")