def quick_sort(s):
    if len(s) <= 1:
        return s

    pivot = s[0]
    left = [x for x in s if x < pivot]
    center = [x for x in s if x == pivot]
    right = [x for x in s if x > pivot]

    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([11, 3, 7, 2, 0, 9, 4]))