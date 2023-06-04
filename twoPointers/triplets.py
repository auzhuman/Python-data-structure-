nums = sorted([-1,0,1,2,-1,-4,-1,1,-2])
nums = [0,0,0]
nums = [7,-1,-6,5,2,-7]
print(nums)

nums = sorted(nums)
print(nums)


# x + y + z = 0
# l,r = 0, len(nums) - 1
# while l <= r:
#     mid = 
triplets = list()

k = len(nums) - 1 
for i in range(len(nums)):
        j = i +1 
        while j < k :

            
             
            sum = nums[i] + nums[j] + nums[k]  
            
            
            if sum == 0 :
                s = [nums[i] , nums[j] , nums[k]  ]
                if s in triplets:
                     continue
                else :
                    triplets.append(s)

                k -= 1
                j += 1

            elif sum < 0 :
                j += 1
                
            else:
                k -= 1


print(triplets)



