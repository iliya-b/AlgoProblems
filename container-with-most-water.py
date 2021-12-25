class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0

        left_index = 0
        right_index = len(height) - 1

        while left_index < right_index:
            min_h = min(height[left_index], height[right_index])
            current_max = min_h * (right_index - left_index)
            maximum = max(maximum, current_max)
            if height[left_index] > height[right_index]:
                right_index -= 1
            else:
                left_index += 1

        return maximum