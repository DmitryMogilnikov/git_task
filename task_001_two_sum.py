class Solution:
    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        hash = {}
        for idx, value in enumerate(nums):
            diff = target - value
            if diff in hash:
                return [hash[diff], idx]
            hash[value] = idx
