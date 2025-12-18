# Time complexity: O(n²)
# Space complexity: O(n²) 

def generate_all_ordered_pairs(nums):
    pairs = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            pairs.append((nums[i],nums[j]))
    return pairs

print(generate_all_ordered_pairs([1,2,3]))

def generate_distinct_ordered_pairs(nums):
    pairs = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                pairs.append((nums[i],nums[j]))
    return pairs

print(generate_distinct_ordered_pairs([1,2,3]))



def generate_unique_pairs(nums):
    pairs = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            pairs.append((nums[i],nums[j]))
    return pairs

print(generate_unique_pairs([1,2,3]))



