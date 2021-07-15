

n=int(input())
nums=list(map(int,input().split()))

ori=[0]*23

for i in range(n):
    tmp=nums[i]
    ori[tmp-1]+=1

for j in ori:
    print(j,end=' ')