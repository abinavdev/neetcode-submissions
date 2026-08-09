class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        # Count frequency
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # Sort elements based on frequency
        sorted_elements = sorted(freq, key=freq.get, reverse=True)

        return sorted_elements[:k]


        