
class Node:
    def __init__(self, low, high):
        self.low = low
        self.high = high

        self.count = 0

class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.node = None
        self.left = None
        self.right = None 
    def build(self, left_pointer, right_pointer):
        self.node = Node(self.array[left_pointer], self.array[right_pointer])
        if left_pointer == right_pointer:
            return self

        mid = (left_pointer + right_pointer) // 2
        self.left = SegmentTree(self.array)
        self.left.build(left_pointer, mid)

        self.right = SegmentTree(self.array)
        self.right.build(mid + 1, right_pointer)

        return self

    def query(self, low, high): 
        if self.node.low >= low and self.node.high <= high:
            return self.node.count 
        if self.node.low > high or self.node.high < low:
            return 0 
        return self.left.query(low, high) + self.right.query(low, high)

    def update(self, val): 
        if self.node.low <= val <= self.node.high:
            self.node.count += 1
            if self.left != None:   self.left.update(val)
            if self.right != None:  self.right.update(val)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        tree = SegmentTree(sorted(list(set(nums))))
        tree.build(0, len(tree.array) - 1)
        res = []
        for n in nums: 
            res.append(tree.query(float("-inf"), n - 1))
            tree.update(n)
        return res[::-1]