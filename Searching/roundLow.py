nums = [7,8,9,10,11,0,1,2,3,5,6]
nums = [7,8,9,2,3]
# nums = [7,1,2,3,4]

Output = 0
def roundLow(nums):

    l,r = 0,len(nums)- 1 
    res = nums[0]


    while l <= r:
        if nums[l] < nums[r]:
            res = min(res,nums[l])

            return res
        
        print("nums is ",nums[l:r+1])
        mid = l + (r-l)//2



        res = min(res,nums[mid])
        print("mid",nums[mid])

        print("res",res)
        
            

        if nums[mid] > nums[r]:
            # nums=   nums[start:]
            l = mid+1
        else:
            r = mid -1
    return res

            

        # elif nums[mid] < nums[mid + 1]: 
        #     l = mid+1
        #     print("l",nums[l])
    
print("mins is ",roundLow(nums))
