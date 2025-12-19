# Ex 2
# Find All Subsets of a Set
# -	Problem: Write a recursive function find_subsets(lst) that returns all possible subsets of a given list of unique elements.
# -	Example: find_subsets([1, 2]) should return [[], [1], [2], [1, 2]].

# def find_subsets(lst):
#   def find_subsets_helper(i):
#     if i == len(lst):
#         return [[]]
#     subsets_without = find_subsets_helper(i + 1)
#     subsets_with = [[lst[i]] + subset for subset in subsets_without]
#     return subsets_without + subsets_with
#   return find_subsets_helper(0)

def find_subsets(lst):    
  if 0 == len(lst):
      return [[]]
  first = lst[0]
  subsets_without = find_subsets(lst[1:])
  subsets_with = [[first] + subset for subset in subsets_without]
  return subsets_without + subsets_with

print(find_subsets([1,2]))

