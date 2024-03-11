def merge(arr, l, r, mid):
    a = []
    left = l
    right = mid+1

    while(left <= mid and right <= r):
        if arr[left] <= arr[right]:
            a.append(arr[left])
            left += 1
        else:
            a.append(arr[right])
            right += 1

    while(left <= mid):
        a.append(arr[left])
        left += 1

    while(right <= r):
        a.append(arr[right])
        right += 1

    for i in range(l, r+1):
        arr[i] = a[i-l]
    return arr


def mergeSort(arr: [int], l: int, r: int):
    # Write Your Code Here
    if l < r:
        mid = (l+r)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, r, mid)
    pass
     

def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    arr = list(set(a+b))
    mergeSort(arr, 0, len(arr)-1)
    return arr
    pass
