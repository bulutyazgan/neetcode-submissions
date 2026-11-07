class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        tmp = height[0]
        for i in range(1, len(height)):
            tmp = max(height[i], tmp)
            leftMax[i] = tmp

        rightMax = [0] * len(height)
        tmp = height[-1]
        for i in range(len(height) - 2, 0, -1):
            tmp = max(height[i], tmp)
            rightMax[i] = tmp

        res = 0
        for i in range(1, len(height) - 1):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res