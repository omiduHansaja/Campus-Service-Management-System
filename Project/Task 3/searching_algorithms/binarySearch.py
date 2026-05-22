def binary_search(data, target):
    comparisons = 0
    low = 0  # Set start range
    high = len(data) - 1  # End Range

    # Continue searching while range is valid
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2  # Find middle

        a = data[mid]
        b = target

        # Checking if the middle record matches target
        if (a["Priority"] == b["Priority"] and
            a["RequestDate"] == b["RequestDate"] and
                a["RequestTime"] == b["RequestTime"]):

            return True, comparisons

        # Compare on priority
        if a["Priority"] > b["Priority"]:
            low = mid + 1

        elif a["Priority"] < b["Priority"]:
            high = mid - 1

        # Compare on RequestDate
        else:
            if a["RequestDate"] < b["RequestDate"]:
                low = mid + 1

            elif a["RequestDate"] > b["RequestDate"]:
                high = mid - 1

            else:
                # Compare on RequestTime
                if a["RequestTime"] < b["RequestTime"]:
                    low = mid + 1
                else:
                    high = mid - 1

    # Target not found
    return False, comparisons
