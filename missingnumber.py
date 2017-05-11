import collections


def find_missing(array1, array2):
    if not array1 and not array2:
        # return 0 if both arrays are empty
        return 0

    if sorted(array1) == sorted(array2): # inplace sorting to determine if arrays are equal
        return 0

    hashtable = collections.defaultdict(int)  # create hashtable to count elements

    for elem in array1:
        """ create hashtable counter with each element in array one and its frequency
            creates a new entry for a non existent element every time its accessed
            increments counter if it's accessed more than once
        """
        hashtable[elem] += 1
    # return hashtable

    for el in array2:
        # if element in array2 doesn't exist(i.e. its counter is 0) return the element and end loop
        if hashtable[el] == 0:
            return el

        else:
            # if element in array2 exists, decrement hashtable counter. Takes care of duplicates
            hashtable[el] -= 1

num = find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
print(num)
