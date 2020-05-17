'''
Write a function to merge our lists of orders into one sorted list.

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
'''


def merge_sorted_lists(arr1, arr2):
    '''Time O(nlgn)'''
    return sorted(arr1 + arr2)


def merge_lists(my_list, alices_list):
    # Make a list big enough to fit the elements from both lists
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:
        if current_index_mine >= len(my_list):
            # Case: my list is exhausted
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1
        elif current_index_alices >= len(alices_list):
            # Case: Alice's list is exhausted
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        elif my_list[current_index_mine] < alices_list[current_index_alices]:
            # Case: my item is next
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: Alice's item is next
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list


def merge_lists_DRY(my_list, alices_list):
    '''O(n) time and O(n)O(n) additional space'''

    # Make a list big enough to fit the elements from both lists
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)

        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[current_index_mine] < alices_list[current_index_alices])):

            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: my list is exhausted
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list