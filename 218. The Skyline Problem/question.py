def getSkyline(buildings):
    def divideConquer(left, right):
        if left == right:
            building = buildings[left]
            return [[building[0], building[2]], [building[1], 0]]

        mid = (left + right) // 2
        left_skyline = divideConquer(left, mid)
        right_skyline = divideConquer(mid + 1, right)

        return merge_skylines(left_skyline, right_skyline)

    def merge_skylines(left, right):
        pass

    if not buildings:
        return []

    return divideConquer(0, len(buildings) - 1)
