# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    index = 0
    # TO-DO
    # Compare first element in each list.

    while arrA and arrB:  # While elements are in both aarA and aarB
        if arrA[0] < arrB[0]:  # if the first element in aarA is less
            merged_arr[index] = (arrA.pop(0))  # pop it from aarA and put in merged_aar
        else:
            merged_arr[index] = (arrB.pop(0))  # pop first element of aarB to put in merged_aar
        index += 1

    if not arrA:  # If aarA is empty
      for j in range(index, len(merged_arr)):  # Loop through aarB and add to merged_aar
        merged_arr[j] = (arrB.pop(0))
    else:  # If aarB is empty
      for j in range(index, len(merged_arr)):  # Loop through aarA and add to merged_aar
        merged_arr[j] = (arrA.pop(0))
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
      return arr
    # Split arr in half and repeat until each element is in it's own list
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr




def quicksort(arr):
    # Check if arr has 0 or 1 elements
    # Base case
    if len(arr) < 2:
        return arr
    
    # Start by choosing a pivot (just pick first item for right now)
    pivot = arr[0]

    # Partition the data
    # Storage lists
    left_side, right_side = [], []
    # Loop through items in arr
    for current in arr[1:]:
        # Move all elements smaller than pivot to left side
        if current <= pivot:
            left_side.append(current)
        # Move all element larger than pivot to right
        else:
            right_side.append(current)

    return quicksort(left_side) + [pivot] + quicksort(right_side)
