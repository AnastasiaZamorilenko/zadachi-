def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


nums = input("Введи числа через запятую: ")
nums_lst = [int(num) for num in nums.split(",")]
sorted_lst = bubble_sort(nums_lst)
print("Отсортированный список:", sorted_lst)
