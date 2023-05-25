#time comp = O(nlogn)
def QuickSort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst.pop()
    left = []
    right = []

    for el in lst:
        if el < pivot:
            left.append(el)
        else:
            right.append(el)
    return QuickSort(left) + [pivot] + QuickSort(right)

lst = [21, 1, 5, 6, 8, 12]
print(QuickSort(lst))