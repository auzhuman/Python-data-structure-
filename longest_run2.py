def longest_run(nums):
    nums = sorted(list(set(nums)))
    if len(nums) == 1 :
        return 1
    if len(nums) ==  0 :
        return 0
    cache = set()
    lengths = []
    l,r = 0,1
    while l<=len(nums)-1:
        print("l",l)
        if len(nums)-1 == l:
            if nums[-1]-1 == nums[-2] :
                cache.add(nums[-1])
                lengths.append(len(cache))
                break
            else :
                break
        
        elif nums[l] + 1  == nums[l+1]:
            cache.add(nums[l])
            cache.add(nums[l+1])
            l = l+1


        else :
            cache.add(nums[l])
            lengths.append(len(cache))
            cache.clear()
            l = l+1
    print(lengths)
    return max(lengths)
              

p = longest_run([100,4,200,1,3,2])
print(p)
# nums = sorted(numsA)
# print(nums)
# # nums =[1, 2, 3, 4, 5,6,100,101]


# print(cache)
# print(lengths)
