SIZE = 10


def print_array(numbers):
    for i in range(len(numbers)):
        print(f"numbers[{i}] = {numbers[i]}")


def find_maximum(numbers):
    maximum = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]

    return maximum


def find_minimum(numbers):
    minimum = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] < minimum:
            minimum = numbers[i]

    return minimum


def calculate_sum(numbers):
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]

    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def swap_min_and_max(numbers):
    min_index = 0
    max_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i

        if numbers[i] > numbers[max_index]:
            max_index = i

    temp = numbers[min_index]
    numbers[min_index] = numbers[max_index]
    numbers[max_index] = temp


def copy_array(numbers):
    copy = []

    for i in range(len(numbers)):
        copy.append(numbers[i])

    return copy


def sort_array(numbers):
    sorted_numbers = copy_array(numbers)

    for i in range(len(sorted_numbers) - 1):
        for j in range(len(sorted_numbers) - 1 - i):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                temp = sorted_numbers[j]
                sorted_numbers[j] = sorted_numbers[j + 1]
                sorted_numbers[j + 1] = temp

    return sorted_numbers


def calculate_median(numbers):
    sorted_numbers = sort_array(numbers)
    size = len(sorted_numbers)

    if size % 2 == 0:
        return (sorted_numbers[size // 2 - 1] + sorted_numbers[size // 2]) / 2

    return sorted_numbers[size // 2]


def main():
    numbers = [1, 2, 3, -4, 50, 6, 7, 8, 9, 10]

    print("Original array:")
    print_array(numbers)

    print()
    print(f"Max: {find_maximum(numbers)}")
    print(f"Min: {find_minimum(numbers)}")
    print(f"Sum: {calculate_sum(numbers)}")
    print(f"Avg: {calculate_average(numbers):.2f}")

    print()
    print("Array after swapping minimum and maximum:")
    swap_min_and_max(numbers)
    print_array(numbers)

    print()
    print("Sorted array:")
    sorted_numbers = sort_array(numbers)
    print_array(sorted_numbers)

    print()
    print(f"Median: {calculate_median(numbers):.2f}")


if __name__ == "__main__":
    main()