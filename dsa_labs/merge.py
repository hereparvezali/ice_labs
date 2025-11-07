def merge_sort(arr, start, end):
    if end - start <= 1:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid, end)
    merge(arr, start, mid, end)


def merge(arr, left, mid, right):
    i = left
    j = mid
    temp = []

    while i < mid and j < right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i < mid:
        temp.append(arr[i])
        i += 1

    while j < right:
        temp.append(arr[j])
        j += 1

    for idx, val in enumerate(temp):
        arr[left + idx] = val


if __name__ == "__main__":
    input_str = input("Enter the array: ").strip()
    v = list(map(int, input_str.split()))
    merge_sort(v, 0, len(v))
    for i in v:
        print(i, end=" ")