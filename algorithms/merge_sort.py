def merge_sort_recursive(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    arr1 = merge_sort_recursive(nums[:mid])
    arr2 = merge_sort_recursive(nums[mid:])
    merged = []
    index1 = 0
    index2 = 0
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] < arr2[index2]:
            merged.append(arr1[index1])
            index1 += 1
        else:
            merged.append(arr2[index2])
            index2 += 1
    
    while index1 < len(arr1):
        merged.append(arr1[index1])
        index1 += 1

    while index2 < len(arr2):
        merged.append(arr2[index2])
        index2 += 1
    
    return merged

print(merge_sort_recursive([5,4,3,2,1,7,8,9]))

