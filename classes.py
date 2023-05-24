# # class automobiles:
# #     def __init__(self,type,enginetype):
# #         self.type = type
# #         self.enginetype = enginetype

# #     def aboutAuto(self):
# #         return (f"{self.type},{self.enginetype}")
# # class brand(automobiles):
# #     def __init__(self,type,enginetype,name,price):
# #         super().__init__(type,enginetype)
# #         self.name = name
# #         self.price = price

# #     def infoCar (self):
# #         return (self.name,self.price)

# # c1 = brand("sedan","petrol","chevro",156897)
# # details = c1.aboutAuto()
# # infocar = c1.infoCar()

# # # details.append("this is wrong")
# # infocar.append("this is wrong")
# # print(details,infocar)


# # num = [1,2,3,4,5,6]

# # fruit = "banana"
# # # for i in (fruit):



# # def justfun(num):
# #     return lambda a : num * a

# # doubler = justfun(2)
# # print(doubler(3))

# thislist = ["apple", "banana", "cherry"] # note the double round-brackets
# # print(thislist)

# # thislist.append("mango")

# # thislist.insert(2,"coconut")
   
# # otherf = set(("pear", "watermelon"))
# # print(type(otherf))
# # thislist.extend(otherf)
# # thislist.pop(1)
# # print(thislist)
# # newlist = [x for x in thislist if "a" not  in x]
# # print(newlist)
# def myfunc(n):
#     return abs(n-50)

# # thislist = [100,50,65,23]
# # for i in range(len(thislist)):
# #     # print(i)
# #     print(myfunc(thislist[i]))
# # # thislist.sort(key=myfunc)
# thislist.reverse()
# # print(thislist)
# # name = "humaN Singh hitang"
# # print(name.lower())

# # name = ["ram","hari","sita"]
# # print(sorted(name))
# # name.sort()
# # print(name)
# set1 = {"ram","hari","sira","gita"}
# set2 = {"ram","rupesh","rita","hari"}
# # x = set1.intersection(set2)
# set1.add("james")
# set1.pop()
# # print(set1)


# set3 = {
#     "name" : "ram",
#     "age" : 19,
#     "height" : 5.4


# }
# for x in set3.items():
#     print(x)
# # print(set3.items())
# # print(set3["ram"])

# print(len(set3))


# sum of numbers within in a list
# def twosum(number,target):
#     l,r = 0,len(number) - 1
#     while l < r :
#         sum = number[l]+number[r]
#         if sum  == target:
#             return l+1,r+1
#         elif sum >target :
#             # if sum of current index is greater than update right
#             r = r-1
#         else:
#             l = l+1
# print(twosum([-2,0,7,11,15,22],20))
# s = ["H"]
# s = ["h","e","","l","","","o"] # olleh
# 12345 = -1,-2
# y = len(s)
# s.pop(1)
# print(s)
# print(y)
# for i in range(y): 

s = "Ram  is kum "
print(len(s))
def reverseFun(s):
    i= 0
    while i < len(s)//2 :
        s[i],s[-i-1] = s[-i-1],s[i]
        i += 1 
    return s

splitarr = s.split()
# print(type(splitarr))
print(splitarr)
for i in range(len(splitarr)):
    splitarr[i] = "".join(reverseFun(list(splitarr[i])))
p = " ".join(splitarr)
print(p)
# revStr = ""
# count = 0
# spacecount = 0
# for i in s :  
#     print(i)
#     if i == " " or count == len(s)-1 :
#         r = "".join(reverseFun(list(s[spacecount:count])))
    
       
#         if spacecount == 0:
#             revStr = revStr+r
#         else:
#             revStr = revStr+" "+r
#         spacecount = count+1
#     count += 1 
#     s= "".join(r)
#     print("r is ",s)
#     print(spacecount,count)

# print(revStr)
        





        
            
      


    
  
        