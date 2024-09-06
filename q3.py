def max_rob(nums):
    sum1=0
    for num in nums[0::2]:
        sum1 += num

    sum2= 0
    for num in nums[1::2]:
        sum2 += num

    return max(sum1 , sum2)

nums = [2,7,9,3,1]
max = max_rob(nums)
print(max)
