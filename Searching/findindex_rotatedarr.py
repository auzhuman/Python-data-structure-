def search(nums: list[int], target: int) -> int:
    l,r = 0,len(nums) -1
    # if target not in nums:
    #     return -1

    while l <=r :
        print(nums[l:r+1])

        mid = l + (r-l) //2

        if nums[mid] == target :
            return mid
        
        if nums[l] < nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid +1 
            else :
                r = mid -1 
        else :
            if target > nums[mid] :
                l = mid +1
            elif target > nums[r]:
                r = mid -1
            else :
                l = mid -1



    
    






nums =[4,1,2,3]
# nums = [4,5,6,7,8,1,2]
target = 3

print("index is ",search(nums,target))



        