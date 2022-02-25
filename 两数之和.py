class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_len = len(numbers)
        left = 0
        right = numbers_len -1
        while (left< right):
            sum = numbers[left]+numbers[right]
            if sum >target:
                right =right-1
                continue
            if sum < target:
                left = left +1
            if sum ==target:
                return [left,right]