def shifter_right(arr,i,value):

    for index in range(len(arr)-1,i-1,-1):
        print(index)
        arr[index] = arr[index -1]

    arr[i] = value
    return arr
arr = [1,2,3,4,5,6,7,0]
p = shifter_right(arr,1,6)
print(p)