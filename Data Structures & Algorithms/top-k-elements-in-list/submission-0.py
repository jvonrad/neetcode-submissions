class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        k_most_frequent = sorted(counts, key = lambda x:counts[x],        reverse=True)
        return k_most_frequent[:k]

        