# Trapping rain water 
# Trapping Rainwater Problem states that given an array of n non-negative integers arr[] representing an elevation map where the width of each bar is 1, compute how much water it can trap after rain. 
# Input: arr[] = {3, 0, 1, 0, 4, 0, 2}
# Output: 10
# Explanation: The expected rainwater to be trapped is shown in the above image.

# Tasks:
# 1.	Write a brute force solution
# 2.	Write an efficient solution in O(n)
# 3.	Solve the problem but now return the max amount of water that can be trapped between 2 buildings

# 1.	Write a brute force solution

def get_total_water_brute_force(arr):
    total = 0
    for i in range(len(arr)):
        left_slice = arr[:i]
        right_slice = arr[i+1:]
        max_left = max(left_slice) if len(left_slice)>0 else -1
        max_right = max(right_slice ) if len(right_slice )>0 else -1
        min_bar= min(max_left,max_right)
        if min_bar > arr[i]:
            total+=min_bar-arr[i]
    return total

print(get_total_water_brute_force([3, 0, 1, 0, 4, 0, 2]))


def get_total_water(arr):
    total = 0
    n = len(arr)
    left = [-1]*n
    right = [-1]*n
    for i in range(1,n):
        left[i] = max(left[i-1],arr[i-1])
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1],arr[i+1])
    for i in range(len(arr)):
        max_left = left[i]
        max_right = right[i]
        min_bar= min(max_left,max_right)
        if min_bar > arr[i]:
            total+=min_bar-arr[i]
    return total

print(get_total_water([3, 0, 1, 0, 4, 0, 2]))
arr = [1, 2, 3, 4, 5]
print(get_total_water_brute_force(arr))
print(get_total_water(arr))

        





