# Second biggest 
# find the second biggest element in an array of numbers

def find_second_biggest(nums):
    if len(nums) < 2:
        return None
    max1 = nums[0] if nums[0] > nums[1] else nums[1]
    max2 = nums[1] if nums[1] > nums[0] else nums[0]
    for i in range(2,len(nums)):
        if nums[i]>max1:
            max2 = max1
            max1 = nums[i]
        elif nums[i]>max2:
            max2 = nums[i]
    return max2

print(find_second_biggest([]))
print(find_second_biggest([1]))
print(find_second_biggest([1,2,3,4,5,6]))
print(find_second_biggest([1,2,3,4,5]))
