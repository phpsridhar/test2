def solution(A):
    # Remove non-positive integers and duplicates
    A = list(set(filter(lambda x: x > 0, A)))

    def find_missing_recursive(arr, start, end):
        if not arr or arr[0] != start:
            return start

        if len(arr) == 1:
            return start + 1

        mid = (start + end) // 2
        left_chunk = [x for x in arr if x <= mid]
        right_chunk = [x for x in arr if x > mid]

        if len(left_chunk) == mid - start + 1:
            return find_missing_recursive(right_chunk, mid + 1, end)
        else:
            return find_missing_recursive(left_chunk, start, mid)

    if not A:
        return 1

    return find_missing_recursive(A, 1, len(A))
