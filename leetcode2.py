nums = [1,2,3,4,5,6,7] 
# nums = [-1,-100,3,99]    #7-3 = 4,
# nums = [1,2]
k = 3#(no of rotation)
l = len(nums) - k 


num = []
for i in range(l,len(nums)):
    num.append(nums[i])
print(num)
for i in range(0,l):
    num.append(nums[i])
nums = num


print(nums)