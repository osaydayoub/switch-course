# Find the common elements between 2 arrays.
def get_common_elements(lst1,lst2):
    common_elements = set()
    set1 = set(lst1)
    for element in lst2:
        if element in set1:
            common_elements.add(element)
    return list(common_elements)