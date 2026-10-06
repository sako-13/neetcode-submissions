class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        s = []
        for i,temp in enumerate(temperatures):
            while s and temperatures[s[-1]] < temp:
                prev = s.pop()
                result[prev] = i-prev
            s.append(i)

        return result
