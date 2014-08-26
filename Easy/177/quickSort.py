from random import randrange

def quicksort(array):
    lesser = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[randrange(len(array)-1)]
        for x in array:
            if x < pivot:
                lesser.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(lesser)+equal+quicksort(greater)
    else:
        return array

array = [5, 12, -3, 570, -91]
print quicksort(array)
