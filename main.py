nums1 = [1, 3]
nums2 = [2]


def medians(nums1, nums2):
    global nums
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)

    if n % 2 == 0:
        res = (nums[int(n / 2 - 1)] + nums[int(n / 2)]) / 2
    else:
        res = nums[int((n + 1) / 2 - 1)]
    return res


print(f'Вход: nums1 = {nums1}, nums2 = {nums2}\n'
      f'Вывод: {medians(nums1, nums2)}\n'
      f'Пояснение: объединеный список = {nums}, медиана {medians(nums1, nums2)}')
