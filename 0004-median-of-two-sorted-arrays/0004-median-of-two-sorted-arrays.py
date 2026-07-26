class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = nums1 + nums2
        arr.sort()

        n = len(arr)

        if n % 2 == 1:
            return float(arr[n // 2])
        else:
            return (arr[n // 2 - 1] + arr[n // 2]) / 2