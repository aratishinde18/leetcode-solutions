class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = -1
        
        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        # Step 2: If pivot exists, find the successor to swap with
        if pivot != -1:
            for i in range(n - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    # Swap pivot and its successor
                    nums[pivot], nums[i] = nums[i], nums[pivot]
                    break
        
        # Step 3: Reverse the suffix elements after the pivot index
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1  # Corrected from right += 1
