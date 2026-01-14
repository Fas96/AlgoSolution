class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, length in squares:
            events.append((y, 1, x, x + length))
            events.append((y + length, -1, x, x + length))

        events.sort()

        active_intervals = []  
        prev_y = events[0][0]
        total_area = 0
        horizontal_slices = [] 

        def union_width(intervals):
            intervals.sort()
            total_width = 0
            rightmost = -10**30
            for left, right in intervals:
                if left > rightmost:
                    total_width += right - left
                    rightmost = right
                elif right > rightmost:
                    total_width += right - rightmost
                    rightmost = right
            return total_width

        for y, event_type, x_left, x_right in events:
            if y > prev_y and active_intervals:
                height = y - prev_y
                width = union_width(active_intervals)
                horizontal_slices.append((prev_y, height, width))
                total_area += height * width

            if event_type == 1:
                active_intervals.append((x_left, x_right))
            else:
                active_intervals.remove((x_left, x_right))

            prev_y = y

        half_area = total_area / 2
        accumulated_area = 0

        for start_y, height, width in horizontal_slices:
            slice_area = height * width
            if accumulated_area + slice_area >= half_area:
                return start_y + (half_area - accumulated_area) / width
            accumulated_area += slice_area

        return float(prev_y)
