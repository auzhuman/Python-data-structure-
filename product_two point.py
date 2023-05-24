nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
# product = 1


product = [1]*len(nums)
left_arr ,right_arr = nums[0],1
for i in range(1,len(nums)):
    print(left_arr)
    product[i] = left_arr
    left_arr *= nums[i]

print(product)
   
for i in range(len(nums)-1,-1,-1):
    product[i] *= right_arr  
    right_arr *= nums[i]  
  
  



print(product)