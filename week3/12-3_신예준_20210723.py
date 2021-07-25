class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.list = nums
        self.index = k
    def add(self, val: int) -> int:
        self.list.append(val)
        self.list.sort(reverse=True)
        return self.list[self.index-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
