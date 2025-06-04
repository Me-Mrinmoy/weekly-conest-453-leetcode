class Solution:
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        result = []

        for i in range(m - k + 1):
            row_result = []
            for j in range(n - k + 1):
                values = []
                # Extract k x k submatrix
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.append(grid[x][y])

                unique_vals = sorted(set(values))
                if len(unique_vals) <= 1:
                    row_result.append(0)
                else:
                    min_diff = float('inf')
                    for z in range(1, len(unique_vals)):
                        min_diff = min(min_diff, abs(unique_vals[z] - unique_vals[z - 1]))
                    row_result.append(min_diff)
            result.append(row_result)

        return result
