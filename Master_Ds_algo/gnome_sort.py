# gnome sort is similar to bubble sort.
# Difference is we go back to last step after swapping the numbers
import random

def gnome_sort(numbers: list[int]) -> list[int]:
    len_numbers = len(numbers)
    index = 0

    while index < len_numbers:
        if index == 0:
            index = index + 1

        if numbers[index] >= numbers[index-1]:
            index += 1
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index -= 1

    return numbers

if __name__ == '__main__':
    nums = [random.randint(0, 100) for _ in range(10)]
    print(nums)
    print(gnome_sort(nums))