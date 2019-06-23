def quick_sort(arr):
    if arr == []:
        return []
    else:
        first = arr[0]
        left = quick_sort([l for l in arr[1:] if l < first])
        right = quick_sort([r for r in arr[1:] if r >= first])
    return left + [first] + right


if __name__ == '__main__':
    arr = [3, 1, 15, 4, 30, 23, 2]
    result_list = quick_sort(arr)
    print(result_list)
