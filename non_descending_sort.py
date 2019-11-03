def non_descend_sort(input_array):
    """
    sorts array into non-descending order and counts the number of swaps it took
    to do so.
    """
    swap_count = 0

    while True:
        # We'll need a copy of our array to loop over so we're not modifying
        # the same array we're looping over.
        input_array_copy = input_array[:]

        # This will become True if we've swapped any values.
        swap_indicator = False

        # Using enumerate here will provide us with the
        # index of each array value and the value itself.
        for index, value in enumerate(input_array_copy[:-1]):
            
            # check if the next value in the array is less than the current value
            if input_array_copy[index + 1] < value:

                # Save the current and next array values to temporary variables
                higher_value = input_array[index]
                lower_value = input_array[index + 1]

                # Then swap the places of ↑ those ↑ values in the array
                input_array[index] = lower_value
                input_array[index + 1] = higher_value

                swap_count += 1
                swap_indicator = True

        if not swap_indicator:
            break

    print(input_array)
    print("Swap Count: " + str(swap_count))



# Some random lists for testing with.
test_list_1 = [1, 2, 3, 4, 5, 1, 2, 2, 1, 2, 3, 3, 23, 23, 1, 21,2, 12, 1, 4, 24, 24]
test_list_2 = [54, 32, 234234, 234, 12, 123, 23, 1, 2, 3, 3, 3, 3]
test_list_3 = [1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2]

non_descend_sort(test_list_1)
print()
non_descend_sort(test_list_2)
print()
non_descend_sort(test_list_3)
print()
