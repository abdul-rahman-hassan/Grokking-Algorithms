"""Module for using selection sort"""


def find_smalllest(arr: int) -> list:
    """selection sort"""
    smallest = arr[0]
    smallest_index = 0
    for i, value in enumerate(arr):
        if value < smallest:
            smallest = value
            smallest_index = i
    return smallest_index


def selection_sort(arr: int) -> list:
    """selection sort"""
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smalllest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


numbers = [int(x)
           for x in input("Enter the numbers sperated by a space :").split()]
print(selection_sort(numbers))
