# insertion sort after swap, the number is compared to other elements on the left

import random

def insertion_sort(numbers: list[int])->list[int]:
    len_numbers = len(numbers)

    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i-1

        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        
        numbers[j+1] = temp

    return numbers

def bucket_sort(numbers: list[int])->list[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers
    buckets = [[] for _ in range(size)]

    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size-1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []

    for i in range(size):
        print(buckets[i])
        result += buckets[i]
        print(result)

    return result

if __name__ == '__main__':
    nums = [1,5,28,25,100,52,27,91,22,99]
    # nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(bucket_sort(nums))
