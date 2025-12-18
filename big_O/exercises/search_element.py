# Time complexity: O(n)
# Space complexity: O(1)
def contains_element(nums,element):
    for num in nums:
        if(num== element):
            return True
    return False

print(contains_element([1,2,3,4],5))
print(contains_element([1,2,3,4],1))