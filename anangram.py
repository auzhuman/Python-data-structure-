# # Input: 
strs = ["eat","tea","tan","ate","nat","bat",""]
# # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# dictana = {}
# for i in range(len(strs)-1):

#     for j in range(len(strs[i])-1):

#         dictana[strs[i][j]] = 


from collections import defaultdict

# print(strs[1][2])
res = defaultdict(list)
print(res)
for s in strs:
    count = [0] * 26
# s= "eatt"
    for c in s:
        count [ord(c) - ord("a")] += 1
    res[tuple(count)].append(s)
# print(res.values())
print(res)