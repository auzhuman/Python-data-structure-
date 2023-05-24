
array = ["c","a","f","b","o","e"]
lenth = len(array)

for i in range(lenth):
    def insideSorter(i,array):
        j = i-1
        while(j > 0):
            if array[j] < array[j-1]:
                array[j],  array[j-1] = array[j-1] , array[j]
                j = j-1
            else :
                break
        return array

    if i == lenth - 1:
        insideSorter(i,array)
    else :
        if array[i+1] < array[i]:
            array[i],  array[i+1] = array[i+1] , array[i]
            insideSorter(i,array)

    print(array)


# j used so list doesn,t go out of IndexError
for i in range(1,lenth):
    
    j = i-1
    while j >= 0 and array[j] > array[j+1]:
        # print(array)
        array[j] , array[j+1] = array[j+1] , array[j]
        j=j-1
print(array)
