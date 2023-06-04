def binarySearch(arr:list,target:int):
    l,r = 0,len(arr)-1

    while l<= r :
        mid = l+(r-l)//2

        if arr[mid] < target :
            l = mid+1 
        elif arr[mid] > target:
            r = mid -1

        else :
            return mid

listofnumber,target =[1,2,3,4,5],6
print("index of  number ",target ,"is ->", binarySearch(listofnumber,target))