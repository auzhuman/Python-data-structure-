# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]



"""iterate through the list compare zeroes if there is zeroes then
 replace it  by the next element and append a zero at last of the list 
"""

 
# zero_pos = 0
# for i in range(len(nums)):
#     print("i is ",i)
   
#     print("zeros_pos ",zero_pos )
#     if nums[i] != 0:
           
#             print( nums[i], nums[zero_pos])
#             nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
#             print("nums[",i,"]",nums[i],"nums[",zero_pos,"]",nums[i])
#             zero_pos += 1 
nums = [0,1,0,3,12]
l = len(nums)
zerospos = 0
for i in range(l):
    print(i)
  
    if nums[i] != 0:
        
        nums[i],nums[zerospos] = nums[zerospos],nums[i]
        zerospos += 1
        print(nums)
        
                

print(nums)
# i =0
# nums[0] = 0
# zeros_pos = 0

# i=1
# nums[1] = 1

# nums[1] = 0
# nums[0] = 1 
# zero_pos = 1
# i = 2
# nums[2] = 0
# zero_pos = 1



