def merge_sort(data):

    # If the list has one or no elements
    if len(data) <= 1:
        return data, 0

    # Spliting the list into two parts
    middle = len(data) // 2

    left_part = []
    right_part = []

    for i in range(len(data)):
        if i < middle:
            left_part.append(data[i])
        else:
            right_part.append(data[i])

    left_part, left_comparisons = merge_sort(left_part)
    right_part, right_comparisons = merge_sort(right_part)

    # Merge two parts
    merged, merge_comp = merge(left_part, right_part)

    # Number of comparisons
    total_comp = left_comparisons + right_comparisons + merge_comp

    return merged, total_comp


def merge(left, right):
    result = []  # List to store results
    comparisons = 0
    i = 0
    j = 0

    # Compare elements from both sides
    while i < len(left) and j < len(right):
        comparisons += 1

        a = left[i]
        b = right[j]

        # Compare on priority
        if a["Priority"] > b["Priority"]:
            result.append(a)
            i += 1

        elif a["Priority"] < b["Priority"]:
            result.append(b)
            j += 1

        # If priority equals, then check requestDate
        else:
            if a["RequestDate"] < b["RequestDate"]:
                result.append(a)
                i += 1

            elif a["RequestDate"] > b["RequestDate"]:
                result.append(b)
                j += 1

            # If priority equals, then check requestTime
            else:
                if a["RequestTime"] <= b["RequestTime"]:
                    result.append(a)
                    i += 1
                else:
                    result.append(b)
                    j += 1

    # Add remaining elements from left part(list)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining elements from right part(list)
    while j < len(right):
        result.append(right[j])
        j += 1

    # Return sorted data and comparisons
    return result, comparisons
