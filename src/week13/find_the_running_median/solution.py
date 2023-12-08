#!/bin/python3
import heapq
import os


#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


class MaxHeapObject:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        if not isinstance(other, MaxHeapObject):
            raise ValueError("cannot compare")
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val


class MaxHeap:

    def __init__(self):
        self.max_heap = []

    def push(self, val):
        heapq.heappush(self.max_heap, MaxHeapObject(val))

    def pop(self):
        max_object = heapq.heappop(self.max_heap)
        return max_object.val

    def __len__(self):
        return len(self.max_heap)


class MinHeap:

    def __init__(self):
        self.min_heap = []

    def push(self, val):
        heapq.heappush(self.min_heap, val)

    def pop(self):
        return heapq.heappop(self.min_heap)

    def __len__(self):
        return len(self.min_heap)


class Median:

    def __init__(self):
        #  to store larger number half
        self.right_median = MinHeap()
        #  to store smaller number half
        self.left_median = MaxHeap()

    def insert(self, input_value):
        if len(self.right_median) == 0 and len(self.left_median) == 0:
            self.right_median.push(input_value)
            return

        if len(self.right_median) > len(self.left_median):
            compare_with = self.right_median.pop()
        else:
            compare_with = self.left_median.pop()

        if input_value < compare_with:
            self.left_median.push(input_value)
            self.right_median.push(compare_with)
        else:
            self.right_median.push(input_value)
            self.left_median.push(compare_with)

    def current_median(self):
        if len(self.right_median) == len(self.left_median):
            min_heap_value = self.right_median.pop()
            max_heap_value = self.left_median.pop()
            self.right_median.push(min_heap_value)
            self.left_median.push(max_heap_value)
            median = (min_heap_value + max_heap_value) / 2
        else:
            extra = self.right_median.pop()
            self.right_median.push(extra)
            median = float(extra)

        return median


def running_median(entries):
    results = []
    median = Median()
    for item in entries:
        median.insert(input_value=item)
        current_median = median.current_median()
        print(current_median)
        results.append(current_median)

    return results


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = running_median(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


if __name__ == '__main__':
    main()
