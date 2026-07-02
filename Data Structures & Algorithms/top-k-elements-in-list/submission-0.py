class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1

        Sorted_lst=sorted(d, key=d.get, reverse=True)

        return Sorted_lst[:k]
