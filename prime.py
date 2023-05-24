# n = 5
# prime= []
# not_prime = []
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j == 0:
#             not_prime.append(i)
#     if i not in not_prime:  
#         prime.append(i)
# print(prime,not_prime)

# a = [1,2,3,4]
# a.append(5)
# print(a)
# a.pop()
# print(a)

# python lambda

# def lamfun(n):
#     return lambda a : a * n

# funa = lamfun(2)
# print(funa(3))



# a = lambda g : g +2
# print(a(2))


# python type function

# def innn(a : int) -> int :
#     if a == "nine":
#         return "n"

# # print(innn("nine"))


# hello: str = "hello world!"

# def add(x: int, y: int) -> int:
#     return x,y

# new_val: int = add("nine", 4)
# print(new_val)

left,right = 3 ,4
mid  = left + (right-left) // 2 
mid2 = (left + right) // 2 
print(mid,mid2)
# print(5//2)
