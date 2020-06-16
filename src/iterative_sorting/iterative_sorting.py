# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j



        # TO-DO: swap
        if i != smallest_index:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    num_checks = len(arr) - 1
    # Loop through the items in the list. 
    # Each loop will loop through one less than the time prior
    # since the highest value moves to the end in each iteration.
    for j in range(len(arr)-1):  # Run through the loop (n-1) times
        for i in range(num_checks): # Decrement the number of checks needed with each loop
            left_item, right_item = arr[i], arr[i+1]

    # Compare the first value with the second value.
    # If the left value is greater than the right value, swap their indices.
    # If not, move to the next pair.
            if left_item > right_item:
                arr[i], arr[i+1] = right_item, left_item

        num_checks -= 1
    # Continue this until looping through (n-1) times.
    # Since the highest value is moved to the end with each iteration the
    # end can be adjusted to one less the prior length after each pass. 

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr