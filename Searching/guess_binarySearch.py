def binarysearch(l,r):
    while l<=r :
        mid = l + (r-l)//2
        
        p = input(print("is the number greater or smaller than ->",mid))
        if p == "greater":
            l = mid +1 
            
        elif p == "smaller":
            r= mid -1
            
        else :
            print("the number is " ,mid)
            break
    return -1







binarysearch(1,100)

# 8
