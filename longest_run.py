nums = [100,4,200,1,3,2,300,101,301,201]
numsSort = sorted(nums)
print(numsSort)

cache = set()
longest = dict()
lengths = list()


for i in range(len(numsSort)):
    
    if i == len(numsSort)-1:
        break


    l,r= numsSort[i]+1,numsSort[i+1]
    print("l,r",l,r,i)

    # add every value to set
    cache.add(numsSort[i])
    if l == r:
        cache.add(numsSort[i+1])
    else :
        lengths.append(len(cache))
        longest[len(cache)] = set(cache)
        cache.clear()
         


print("set",cache)
print("longest list ",lengths)
print(" dict is ",longest)

# [1, 2, 3, 4, 100,101,200]


# except using sort we can use if the next value is in  the list