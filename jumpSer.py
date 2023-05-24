# Python3 code to implement Jump Search
import math
def jumpSer(nums:list,target:int) -> int:
  step = int(math.sqrt(len(nums)))

  jump = step

  for i in range(len(nums)):
    if nums[jump] == target:
    # if values match at jump return jump index
      return jump,i,1

    """
    if value in jump index greater than target 
    value lies between previous jump and laterone so perform linear 
    search
    """
    if nums[jump] > target:
    
    
      for j in range((jump-step),jump):
        if nums[j] == target:
          return j,i,2
      
    jump += step
    

a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print(len(a))
target = 55
a = jumpSer(a,target)
print(a)
          
        
      
  