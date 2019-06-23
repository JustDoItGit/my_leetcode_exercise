def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):  # 从右往左
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [3, 1, 15, 4, 30, 23, 2]
    result_list = insert_sort(arr)
    print(result_list)
