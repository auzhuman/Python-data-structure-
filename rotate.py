class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)-k 


        num = []
        for i in range(l,len(nums)):
            num.append(nums[i])
       
        for j in range(0,l):
            num.append(nums[j])

        nums[:] = num.copy()
        print(nums)
        # k = k % l
        # nums[l - k:],nums[:l-k]  =nums[:l-k] ,nums[l - k:]

p1 = Solution()
j = p1.rotate([1,2,3],2)
# print(j)