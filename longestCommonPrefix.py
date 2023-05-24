 
strs = ["flower","flow","floight"]
# Output = "fl"
# strs = ["dog","racecar","car"]
# strs =[""]
# print(len(strs[0]))
# strs = ["dog","racecar","car"]
# strs = ["reflower","flow","flight"]
# strs = ["car","cir"]


# longpre(strs)
def longpre(strss):
    strs = sorted(strss)
    temp = strs[0]
    
    # if len(strs) <= 1:
    #     return temp
    
    for i in range(1,len(strs)):
        prefix = []
        
        for j in range(len(temp)): 
            print(strs[i][j] ,"temp is ",temp[j])   
            if strs[i][j] == temp[j]:
                prefix += strs[i][j]
            else :
                break
            print("prefix",prefix)
        temp = prefix
    s = "".join(temp)
    return(s)
p=longpre(strs)
print("prefix",p)