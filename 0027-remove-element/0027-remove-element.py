class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to keep track of the position for non-val elements
        k = 0
        
        for i in range(len(nums)):
            # If the current element is not the target value
            if nums[i] != val:
                # Place it at the k-th index and advance k
                nums[k] = nums[i]
                k += 1
                
        return k
