class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            area = self.calculateArea(heights, l, r)
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
    
    def calculateArea(self, heights, l, r):
        return (r - l) * min(heights[r], heights[l])