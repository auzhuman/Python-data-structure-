import math
def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    print("piles is ",piles)

    max_is = max(piles)


    


    l,r = math.ceil(sum(piles)/h),max_is
            # 
    while l <= r :
        mid = l + (r-l) //2
        print(mid)
        
        


        kTimeime =sum([math.ceil(i/mid) for i in piles])




        print("hours is",kTimeime)
        # print(kTimeime * h)
        if kTimeime <= h :
            r = mid -1
        else :
            l = mid+1

    print( "res is ",l)



piles = [3,6,7,11]
h = 8

# piles = [30,11,23,4,20]
# h = 6
minEatingSpeed(piles,h)