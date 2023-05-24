#ternerary search uses two mid points to find the element in an sorted array divided into three
def tern_ser(nums:list,target:int)-> int:
  l,r = 0,len(nums)-1
  i = 0
  while r>=l:
    i += 1
    mid1 = l+(r-l)//3
    mid2 = r-(r-l)//3
    if nums[mid1] == target:
    #   print(mid1)
      return mid1,i
    if nums[mid2] == target:
    #   print(mid2)
      return mid2,i

    
    if target < nums[mid1]  :
        # number lies between l,mid1
      r = mid1 - 1
    elif target > nums[mid2]:
      # number lies between mid2 and r
      l = mid2 +1
    else:
        # number lies between mid1 and mid2
      l=mid1 + 1
      r = mid2 -1
  return False
      
      
      


    # break
  # print(mid1,mid2)


a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a.sort()
target = 10
a = tern_ser(a,target)
print(a)

