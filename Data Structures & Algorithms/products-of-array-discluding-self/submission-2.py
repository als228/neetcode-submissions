class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff = deque([1])

        for i in range(len(nums)-1):
            pref.append(pref[-1] * nums[i])
        for i in range(len(nums)-1, 0, -1):
            suff.appendleft(suff[0] * nums[i])
        
        for i in range(len(nums)):
            nums[i] = pref[i] * suff[i]
        
        return nums