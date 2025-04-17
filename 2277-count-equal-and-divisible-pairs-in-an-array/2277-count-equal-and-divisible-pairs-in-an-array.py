class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        num_to_indices = defaultdict(list)
        for idx, num in enumerate(nums):
            num_to_indices[num].append(idx)
        
        ans = 0
        for indices in num_to_indices.values():
            freq = defaultdict(int)
            for i in indices:
                gcd_i_k = math.gcd(i, k) 
                for j_gcd, count in freq.items():
                    if (i * j_gcd) % k == 0:
                        ans += count
                freq[gcd_i_k] += 1
        return ans