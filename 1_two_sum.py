"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums, target):
    if nums.count(target/2) >= 2:
        result = [idx for idx, elem in enumerate(nums) if elem == target / 2]
        return result
    else:
        diffs = [target - num for num in nums]
        matches = [x for x in diffs if (x in nums and x != target/2)]
        result = [idx for idx,elem in enumerate(nums) if elem in matches]
        return result


def test():
    nums_list = [[2, 7, 11, 15], [3,2,4], [3, 3]]
    target_list = [9, 6, 6]

    for i in range(len(target_list)):
        result = twoSum(nums_list[i], target_list[i])
        print(f'nums: {nums_list[i]} target:{target_list[i]} result: {result}')


test()