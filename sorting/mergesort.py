"""While a recursion call is made first the nested recursion is tackled than it flows to the outer one"""
def merge(l,r):
    # print("l,r is ",l,r)
    result = []
    i,j = 0,0


    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else :
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    # print("result from merge",result)
    return result

def mergeSort(arrays:list):

    # print("arrays is and call is made",arrays,i)
    e = len(arrays)

    if e <= 1:
        return arrays
    mid = int( e // 2)
  
    # print(arrays)
    l = mergeSort(arrays[:mid])
    r = mergeSort(arrays[mid:])
    return merge(l,r)


k = [1,6,5,3,2,0]
p= mergeSort(k)
print(p)
