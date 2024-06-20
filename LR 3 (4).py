from random import randint
def k_search(nums, low, high, k):
    if low == high:
        return nums[low]
    left = low
    right = high
    pivot = nums[(low + high) // 2]
    while left <= right:
        while nums[left] < pivot:
            left += 1
        while nums[right] > pivot:
            right -= 1
        if left >= right:
            break
        nums[right], nums[left] = nums[left], nums[right]
        right -= 1
        left += 1
    if k <= right - low + 1:
        new_low = low
        new_high = right
        new_k = k
    else:
        new_low = right + 1
        new_high = high
        new_k = k - (right - low + 1)
    return k_search(nums, new_low, new_high, new_k)
arr = [randint(-20, 20) for i in range(10)]
print(f"Список: {arr},\nОтсортированный список: {sorted(arr)}")
k = int(input("Введите k: "))
a = k_search(arr, 0, len(arr) - 1, k)
print(f"{k}-й элемент: {a}")
