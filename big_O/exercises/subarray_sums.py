# Time complexity: O(n²)
# Space complexity: O(n²) 
def compute_all_subarray_sums(nums):
    prefix_sums  = [nums[0]]
    for i in range(1,len(nums)):
        prefix_sums.append(prefix_sums [i-1]+nums[i])   
    
    subarray_sums = []
    for i in range(len(nums)):
        for j in range (i,len(nums)):
            if i==0:
                subarray_sums.append(prefix_sums [j])
            else:
                subarray_sums.append(prefix_sums [j]-prefix_sums [i-1])
    return subarray_sums 

print(compute_all_subarray_sums([1,1,1,1,1]))

# Time complexity: O(n)
def get_total_subarray_sums(nums):
    total_sum = 0
    n = len(nums)
    for index ,value in enumerate(nums):
        appearances  = (index+1)*(n-index) 
        total_sum += value*appearances
    return total_sum 

print(get_total_subarray_sums([1,1,1,1,1]))
print(sum(compute_all_subarray_sums([1,1,1,1,1])))