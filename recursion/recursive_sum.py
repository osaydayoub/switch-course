def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0]+recursive_sum(lst[1:])
print(recursive_sum([1]))
print(recursive_sum([1,1,1]))