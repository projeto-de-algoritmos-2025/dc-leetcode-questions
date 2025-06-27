class Solution(object):
    def getSkyline(self, buildings):
        if not buildings:
            return []

        return self.divide_conquer(buildings, 0, len(buildings) - 1)

    def divide_conquer(self, buildings, left, right):
        if left == right:
            building = buildings[left]
            return [[building[0], building[2]], [building[1], 0]]

        mid = (left + right) // 2
        left_skyline = self.divide_conquer(buildings, left, mid)
        right_skyline = self.divide_conquer(buildings, mid + 1, right)
        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right):
        result = []
        i = j = 0
        left_height = right_height = 0

        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                curr_x = left[i][0]
                left_height = left[i][1]
                i += 1
            elif left[i][0] > right[j][0]:
                curr_x = right[j][0]
                right_height = right[j][1]
                j += 1
            else:
                curr_x = left[i][0]
                left_height = left[i][1]
                right_height = right[j][1]
                i += 1
                j += 1

            max_height = max(left_height, right_height)

            if not result or result[-1][1] != max_height:
                result.append([curr_x, max_height])

        while i < len(left):
            curr_x, left_height = left[i]
            max_height = max(left_height, right_height)
            if not result or result[-1][1] != max_height:
                result.append([curr_x, max_height])
            i += 1

        while j < len(right):
            curr_x, right_height = right[j]
            max_height = max(left_height, right_height)
            if not result or result[-1][1] != max_height:
                result.append([curr_x, max_height])
            j += 1

        return result
