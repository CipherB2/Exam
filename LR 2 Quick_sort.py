from random import randint, choice
def quicksort(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1

    if low < high:
        p = partition(nums, low, high)
        quicksort(nums, low, p)
        quicksort(nums, p + 1, high)
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    left = low
    right = high

    while True:
        while nums[left] < pivot:
            left += 1
        while nums[right] > pivot:
            right -= 1
        if left >= right:
            return right
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
arr = [randint(-20, 20) for i in range(10)]
print(arr)
quicksort(arr)
print(arr)
