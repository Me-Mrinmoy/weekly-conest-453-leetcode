class Solution:
    def checkEqualPartitions(self, nums, target):
        def prod(iterable):
            result = 1
            for x in iterable:
                result *= x
            return result

        n = len(nums)
        seen = set()

        # Try all non-empty subsets
        for mask in range(1, 1 << n):
            subset = [nums[i] for i in range(n) if (mask >> i) & 1]
            if len(subset) == 0 or len(subset) == n:
                continue  # Skip empty or full subsets
            p = prod(subset)
            if p == target:
                seen.add(frozenset(subset))

        # Check all pairs of disjoint subsets with product == target
        seen = list(seen)
        for i in range(len(seen)):
            for j in range(i + 1, len(seen)):
                if seen[i].isdisjoint(seen[j]):
                    return True

        return False
