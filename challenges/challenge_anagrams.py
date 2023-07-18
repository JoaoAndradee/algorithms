def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return (first_string, second_string, False)

    first_string = first_string.lower()
    second_string = second_string.lower()

    sorted_first = sort_string(first_string)
    sorted_second = sort_string(second_string)

    return (sorted_first, sorted_second, sorted_first == sorted_second)


def sort_string(string):
    chars = list(string)
    quicksort(chars, 0, len(chars) - 1)
    return ''.join(chars)


def quicksort(chars_array, start, end):
    if start < end:
        p = partition(chars_array, start, end)
        quicksort(chars_array, start, p - 1)
        quicksort(chars_array, p + 1, end)


def partition(chars_array, start, end):
    pivot = chars_array[end]
    delimiter = start - 1
    for index in range(start, end):
        if chars_array[index] <= pivot:
            delimiter += 1
            chars_array[delimiter], chars_array[index] = (
                chars_array[index],
                chars_array[delimiter]
            )

    chars_array[delimiter + 1], chars_array[end] = (
        chars_array[end],
        chars_array[delimiter + 1]
    )

    return delimiter + 1
