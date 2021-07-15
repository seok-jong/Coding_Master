

n= int(input())

nums = list(map(int,input().split()))

for i in range(n-1,-1,-1):
    print(nums[i],end=' ')
