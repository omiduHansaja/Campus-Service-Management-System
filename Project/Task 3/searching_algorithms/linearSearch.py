def linear_search(data, target):

    comparisons = 0

    # Checking each item in list(data)
    for item in data:
        comparisons += 1

        # Checking if the current item matches target
        if item == target:

            return True, comparisons

    return False, comparisons
