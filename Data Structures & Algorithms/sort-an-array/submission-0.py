from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Base case
        if len(nums) <= 1:
            return nums

        # Find middle
        mid = len(nums) // 2

        # Split array
        left = nums[:mid]
        right = nums[mid:]

        # Recursively sort left and right
        left = self.sortArray(left)
        right = self.sortArray(right)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, left, right):

        result = []

        i = 0
        j = 0

        # Compare elements from left and right
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1

        # Add remaining elements from left
        while i < len(left):
            result.append(left[i])
            i += 1

        # Add remaining elements from right
        while j < len(right):
            result.append(right[j])
            j += 1

        return result