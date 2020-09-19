def keepEvenNUmbers(nums):
    evenNumberList = filter(lambda num: num % 2 == 0, nums)
    return list(evenNumberList)

print(keepEvenNUmbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))