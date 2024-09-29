"""Module for Binary Search"""


def binary_search(arr: any, item: int):
    """binary search implementation"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid
    return mid


numbers = sorted([int(x) for x in input(
    "Enter the numbers sperated by a space :").split()])
target = int(input('Enter the target number: '))

binary_search(numbers, target)
print("The index of the number is: ", binary_search(numbers, target))
