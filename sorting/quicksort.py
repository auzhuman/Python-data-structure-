array = [6,9,2,4,1,3]
# array =[4,6]
# array = [5,9,3,1,2,4,6]
# array = [2,1]
# array = []
"""quick sort compares the last element to other and sorts as pivot after that the element except the pivot is passed 
recursively until a single element is found ..This algo doesn't require extra memory as swap happens within the given array """
def quicksort(array,s,e):
    
    print("passed array",array)
    if e-s < 1 :

        return array
    
    pivot = array[e]

    left = s    
    for i in range(s,e):
    #loop carried to compare with pivot 
        
        
        if array[i] <  pivot :
            array [i] ,array [left] = array [left] ,array [i] 
          
            left = left+1

    array[e] = array[left]
    array[left] = pivot
       
    
    quicksort(array,s,left-1)
    quicksort(array,left+1,e)
    

    return array

sortedarray = quicksort(array,0,len(array)-1)
print("the sorted array is ",sortedarray )