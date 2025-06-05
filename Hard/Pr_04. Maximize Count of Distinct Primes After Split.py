class Solution:
    def maximumCount(self, nums, queries):
        n = len(nums)
        max_val = 10**5 + 1

        # Sieve to mark prime numbers
        is_prime = [False, False] + [True] * (max_val - 2)
        for i in range(2, int(max_val**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, max_val, i):
                    is_prime[j] = False

        # Helper to check primality
        def is_prime_val(x):
            return is_prime[x]

        res = []

        for idx, val in queries:
            nums[idx] = val  # Apply the update

            # Build prefix and suffix prime sets
            prefix_set = set()
            prefix_counts = [0] * n
            for i in range(n):
                if is_prime_val(nums[i]):
                    prefix_set.add(nums[i])
                prefix_counts[i] = len(prefix_set)

            suffix_set = set()
            suffix_counts = [0] * n
            for i in range(n - 1, -1, -1):
                if is_prime_val(nums[i]):
                    suffix_set.add(nums[i])
                suffix_counts[i] = len(suffix_set)

            # Try all valid splits
            max_distinct = 0
            for k in range(1, n):
                max_distinct = max(max_distinct, prefix_counts[k - 1] + suffix_counts[k])

            res.append(max_distinct)

        return res
