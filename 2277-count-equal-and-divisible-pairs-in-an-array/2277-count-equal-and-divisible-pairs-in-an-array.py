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
                required = k // gcd_i_k
                # We need to find j in indices where gcd(j, k) is divisible by required
                # Which simplifies to finding j where (j * gcd_i_k) % k == 0
                # So, j must be such that (j % (k / gcd_i_k)) == 0
                # So, j must be divisible by (k / gcd(gcd_i_k, k / gcd_i_k)) ... ?
                # Alternatively, we can iterate through possible divisors.
                # For now, let's proceed with checking all previous j's.
                for j_gcd, count in freq.items():
                    if (i * j_gcd) % k == 0:
                        ans += count
                freq[gcd_i_k] += 1
        return ans