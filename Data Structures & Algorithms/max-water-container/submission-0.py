class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_container = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            container = width * height

            max_container = max(container, max_container)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_container

