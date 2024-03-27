class Solution:
    def check(self, nums) -> bool:
        n =len(nums)
        rotate = 0
        for i in range(0,n):
            if nums[i]>nums[(i+1)%n]:
                rotate +=1
            if rotate >1:
                return False
        return True
    
obj = Solution()
x = obj.check([11,14,15,1,2,3,4])
print(x)