class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        heights.append(0)

        for i, height in enumerate(heights):

            while stack and heights[stack[-1]] > height:
                index = stack.pop()
                h = heights[index]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                area = h * width
                largest = max(largest, area)
            stack.append(i)

        return largest
