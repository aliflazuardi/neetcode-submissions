class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(elems: List[int], i: int):
            if sum(elems) == target:
                ans.append(elems.copy())
                return
            if i >= len(nums) or sum(elems) > target:
                return
            
            elems.append(nums[i])
            backtrack(elems, i)
            elems.pop()
            backtrack(elems, i + 1)
            

        backtrack([], 0)

        return ans