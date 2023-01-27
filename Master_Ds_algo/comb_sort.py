# swaping: guided by Gap (array length) divided by 1.3 (pre-determined number)
import random

def comb_sort(numbers: list[int]) ->list[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap/1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]
                swapped = True
    
    return numbers

if __name__ == '__main__':
    nums = [random.randint(0, 100) for _ in range(10)]
    print(nums)
    print(comb_sort(nums))