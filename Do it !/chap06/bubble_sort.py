def bubble_sort(arr):
    length = len(arr) - 1

    for i in range(length):
        isSort = False

        for j in range(length-i):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSort = True
        if isSort == False:
            break
    return arr