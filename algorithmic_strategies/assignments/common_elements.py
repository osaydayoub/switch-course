# Find the common elements between 2 arrays.
def get_common_elements(lst1,lst2):
    common_elements = set()
    set1 = set(lst1)
    for element in lst2:
        if element in set1:
            common_elements.add(element)
    return list(common_elements)

# Find the common elements between 3 arrays.
def get_common_elements_3(lst1,lst2, lst3):
    common_elements = set()
    set1 = set(lst1)
    set2 = set(lst2)
    for element in lst3:
        if element in set1 and element in set2:
            common_elements.add(element)
    return list(common_elements)

print(get_common_elements_3([1,2,3],[2,4],[]))
print(get_common_elements_3([1,2,3],[2,4],[2]))


def get_common_elements_duplicates(lst1,lst2,lst3):
    common_elements = []
    dictionary_1 = {}
    for element in lst1:
        if dictionary_1.get(element)!=None:
            dictionary_1[element] += 1
        else:
            dictionary_1[element] = 1
    dictionary_2 = {}
    for element in lst2:
        if dictionary_2.get(element)!=None:
            dictionary_2[element] += 1
        else:
            dictionary_2[element] = 1
    for element in lst3:
        val_1 = dictionary_1.get(element)
        val_2 = dictionary_2.get(element)
        if val_1>0 and val_2>0:
            common_elements.append(element)
            dictionary_1[element] -= 1
            dictionary_2[element] -= 1
    return common_elements

print(get_common_elements_duplicates([1,2,3],[2,4],[]))
print(get_common_elements_duplicates([1,2,3,1],[1,2,4,1],[1,1,2,1]))



    

