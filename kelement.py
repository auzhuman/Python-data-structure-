
def topKFrequent(nums: list[int], k: int) :
        map_dict = dict()
        for i in nums:
            map_dict[i] = 1 + map_dict.get(i,0)
          
        print(map_dict)
        
        index_list = [[]for i in range(len(nums)+1)]
        for key,val in map_dict.items():
            index_list[val].append(key)

        print(index_list)
        res = []
        for i in range(len(index_list)-1,0,-1):
            print(i)

            for n in index_list[i]:
                res.append(n)
                if len(res) == k:
                    return res


        

        # for i in range(len(index_list)):
        #     if


        # return(index_list[])
       
# Input: 
nums = [1,1,1,2,2,2,3,4,5]
k = 4
p = topKFrequent(nums,k)
print(p)
# Output: [1,2]