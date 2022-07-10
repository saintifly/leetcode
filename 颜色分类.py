from typing import List
def sortColors( nums: List[int]) -> None:
    nums_len =  len(nums)
    start_point = 0
    for i in range(nums_len):
        current_num = nums[i]
        if current_num == 0:
            nums[i] = nums[start_point]
            nums[start_point] = current_num
            start_point +=1
    for i in range(start_point,nums_len):
        current_num = nums[i]
        if current_num == 1:
            nums[i] = nums[start_point]
            nums[start_point] = current_num
            start_point += 1
    print(nums)
if __name__ == '__main__':
    inputlist = [2,0,2,1,1,0]
    sortColors(inputlist)


