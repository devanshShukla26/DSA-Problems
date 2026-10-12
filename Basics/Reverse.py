nums=[2,4,1,7,6,3,8,9,5]
def func(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left + 1, right - 1)


def reverseArray(nums,left,right):
    func(nums,1,5)
    return  nums
print(reverseArray(nums,1,5))
