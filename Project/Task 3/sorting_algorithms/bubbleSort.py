def bubble_sort(data):

    # Setting the comparisons to 0
    comparisons = 0

    # Loop through dataset
    for i in range(len(data)):
        for j in range(len(data) - 1):
            comparisons += 1

            # Compare two records next to each other
            a = data[j]
            b = data[j + 1]

            # Swap record if priority level is low
            if a["Priority"] < b["Priority"]:
                data[j], data[j + 1] = data[j + 1], data[j]

            # If priority equals, then check RequestDate
            elif a["Priority"] == b["Priority"]:
                if a["RequestDate"] > b["RequestDate"]:
                    data[j], data[j + 1] = data[j + 1], data[j]

                # If dates are equal, check RequestTime
                elif a["RequestDate"] == b["RequestDate"]:
                    if a["RequestTime"] > b["RequestTime"]:
                        data[j], data[j + 1] = data[j + 1], data[j]

    # Return sorted data and comparisons
    return data, comparisons
