class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        # Count frequency
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        bucket = [[]for _ in range(len(nums)+1)]
        
        for num,count in freq.items():
            bucket[count].append(num)
        new = []
        for count in range(len(nums),0,-1):
            for num in bucket[count]:
                new.append(num)
                if len(new) == k:
                    return new
        # # Sort elements based on frequency
        # sorted_elements = sorted(freq, key=freq.get, reverse=True)

        # return sorted_elements[:k]


        