class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n < 0:
            x = 1/x
            n = abs(n)
        i = 0

        """Maximun Recursion depth exceeds"""
        def power(x,i):
            while i>n:
               
                return 1.00
            print(x)
            i = i+1
            return x * power(x,i)
            
        print(power(x,i))

        
    
# p = Solution()
# p.myPow(0.00001,2147483647)

"""memory error"""
# def mypow(x,n):
#     p = 1
#     for i in range(n):
#         p = p *x
#     print(p)

# mypow(0.00001,2147483647)
import math
def mypow(x:float,n:int) -> float:
        flag = 0
        if x == 0:
            return 0
        elif x < 0:
            x = abs(x)
            flag = 1

            
        answer = round(math.exp(n * math.log(x)),5)

        if abs(n) % 2 != 0  and  flag == 1:
            return(answer*-1)
        else : 
            return(answer)




def pow (x,n):
    print("from default",x**n)


x =-1.00000
n = 2147483647

x = 2.12
n = 3

print(mypow(x,n))
pow(x,n)

# mypow(x = 0.00001,n = 2147483647)


