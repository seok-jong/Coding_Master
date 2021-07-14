#
# 월이 입력될 때 계절 이름이 출력되도록 해보자.
#
# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall


#code

a= int(input())

winter=[12,1,2]
spring=[3,4,5]
summer=[6,7,8]
fall=[9,10,11]

if a in winter:
    print("winter")
elif a in spring:
    print("spring")
elif a in summer:
    print("summer")
else:
    print("fall")