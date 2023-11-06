 def partition(arr):
        pivot = 1
        left, right = [], []
        for num in arr:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)
        return left, right

    # Main function for finding the smallest missing positive integer
    def find_smallest_missing_positive(arr):
        if not arr:
            return 1

        left, right = partition(arr)

        if sum(left) < len(left) * 1:
            return find_smallest_missing_positive(left)
        else:
            return find_smallest_missing_positive(right)

    return find_smallest_missing_positive(A)
