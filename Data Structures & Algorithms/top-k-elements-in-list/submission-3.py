class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        c = []
        for i in nums:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        for i in range(k):
            max = 0
            v = 0
            for key in dic:
                if dic[key] > max:
                    v = key
                    max = dic[key]
            c.append(v)
            del dic[v]
        return c

