# 1.第一题，从一个数组里找出两个相加等于目标数字的元素，并按从小到大的顺序返回符合条件的元素的最小的下标。


def twoSum(nums, target):
    s = set(nums)
    for num in s:
        targetNum = target - num
        index1 = nums.index(num)
        if targetNum in s:
            index2 = nums.index(targetNum)
            if index1 == index2:
                index2 = nums[index1 + 1:].index(targetNum) + index1 + 1
            return [index1, index2]


print(twoSum([0, 4, 3, 0], 0))
