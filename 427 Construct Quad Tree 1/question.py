class Node(object):
    def __init__(
        self,
        val=False,
        isLeaf=False,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        return self._construct_recursive(grid, 0, 0, len(grid))

    def _construct_recursive(self, grid, row, col, size):
        if self._is_uniform(grid, row, col, size):
            val = bool(grid[row][col])
            return Node(val=val, isLeaf=True)

        half_size = size // 2

        top_left = self._construct_recursive(grid, row, col, half_size)
        top_right = self._construct_recursive(grid, row, col + half_size, half_size)
        bottom_left = self._construct_recursive(grid, row + half_size, col, half_size)
        bottom_right = self._construct_recursive(
            grid, row + half_size, col + half_size, half_size
        )

        return Node(
            val=True,
            isLeaf=False,
            topLeft=top_left,
            topRight=top_right,
            bottomLeft=bottom_left,
            bottomRight=bottom_right,
        )

    def _is_uniform(self, grid, row, col, size):
        first_val = grid[row][col]

        for i in range(row, row + size):
            for j in range(col, col + size):
                if grid[i][j] != first_val:
                    return False

        return True
