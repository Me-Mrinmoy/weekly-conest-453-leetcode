from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        litter_positions = {}
        litter_count = 0
        start = None

        # Find start and all 'L' positions
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_positions[(i, j)] = litter_count
                    litter_count += 1

        total_mask = (1 << litter_count) - 1
        visited = set()

        # (x, y, energy left, litter_mask, steps)
        q = deque()
        q.append((start[0], start[1], energy, 0, 0))
        visited.add((start[0], start[1], energy, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            x, y, e, mask, steps = q.popleft()

            if mask == total_mask:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                ne = e - 1

                if 0 <= nx < m and 0 <= ny < n:
                    cell = classroom[nx][ny]
                    if cell == 'X':
                        continue
                    if ne < 0 and cell != 'R':
                        continue
                    if cell == 'R':
                        ne = energy

                    new_mask = mask
                    if cell == 'L':
                        bit = litter_positions.get((nx, ny), -1)
                        if bit != -1:
                            new_mask |= (1 << bit)

                    state = (nx, ny, ne, new_mask)
                    if state not in visited:
                        visited.add(state)
                        q.append((nx, ny, ne, new_mask, steps + 1))

        return -1
