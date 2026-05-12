def quick_sort_median(arr, left, right):
    if left >= right:
        return
    # 三位取中选 pivot
    mid = (left + right) // 2
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    arr[left], arr[mid] = arr[mid], arr[left]
    
    pivot = arr[left]
    i, j = left, right
    while i < j:
        while i < j and arr[j] >= pivot:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= pivot:
            i += 1
        arr[j] = arr[i]
    arr[i] = pivot
    quick_sort_median(arr, left, i-1)
    quick_sort_median(arr, i+1, right)