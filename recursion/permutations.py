# Ex 3
# Write a recursive function that will find all permutations of a list.
# Example:
# For [1,2,3] it should return: 
# [[1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]]

# def find_all_permutations(lst):
#     if len(lst)==0:
#         return [[]]
#     first = lst[0]
#     rest_perms = find_all_permutations(lst[1:])
#     result = []
#     for p in rest_perms:
#         for i in range(len(p)+1):
#             result.append(p[:i]+[first]+p[i:])
#     return result

def find_all_permutations(lst):
    if len(lst)==0:
        return [[]]
    result = []
    for i in range(len(lst)):
        remaining = lst[:i]+lst[i+1:]
        for p in find_all_permutations(remaining):
            result.append([lst[i]]+p)
    return result





print(find_all_permutations([1,2,3]))