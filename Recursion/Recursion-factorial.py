
# def fibo(num):
     

#     while num  == 1:
#          return 1
    
#     return num * fibo(num - 1)
        
0+1+1+2+3+5
# print(fibo(5))
def fibo(n):
    lists = [0,1]
    sum = lists[0] + lists[1]
    for i in range(0,n-1):
        
        lists.append(sum)
        sum = lists[-1] + lists [-2]
    print(lists)
    return lists[n]
# fibo(5)
def findFindbyindex(index):
    return fibo(index)


print(findFindbyindex(10))


# def fibo(n):
#     if n<=1:
#         return n
#     return fibo(n-1) + fibo(n-2)
# p = list()
# for i in range(5):
#     p.append(fibo(i))
# print((p))

