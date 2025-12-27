
def binary_search(nums,num):
    start = 0
    end = len(nums)-1
    mid = len(nums)//2
    while start <= end:
        if nums[mid]>num:
            end = mid-1
            mid = start+(end-start)//2
        elif nums[mid]<num:
            start = mid+1
            mid = start +(end-start)//2
        elif nums[mid]==num:
            return mid
    return -1

print(binary_search([1,2,3,4,5,6,7],7)) 
