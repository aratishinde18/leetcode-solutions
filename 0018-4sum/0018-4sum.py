class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Pruning 1: Smallest sum possible is greater than target
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # Pruning 2: Largest sum possible is less than target
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Pruning 3: Smallest sum possible from here is greater than target
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # Pruning 4: Largest sum possible from here is less than target
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                    
                # Two-pointer search for the remaining two elements
                left, right = j + 1, n - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates for left and right pointers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res
