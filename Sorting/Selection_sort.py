def sele_sort(nums):
    for i in range(len(nums)):
        min=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min]:
                min=j
        nums[i],nums[min]=nums[min],nums[i]
    return nums
nums=[5,7,8,4,1,6,9,2]
print(sele_sort(nums))