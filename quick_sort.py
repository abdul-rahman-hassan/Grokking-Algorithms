"""quick sort algorithm"""


def quick_sort(nums):
    """implementation of quick sort"""
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [x for x in nums[1:] if x <= pivot]
        more = [x for x in nums[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)
