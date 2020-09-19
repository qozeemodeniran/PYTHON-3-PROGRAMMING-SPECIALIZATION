"""Now consider another common pattern: going through a list and 
keeping only those items that meet certain criteria. 
This is called a filter.
--We'll write a function that returns even numbers from a
listof 1-10"""

def keepEvenNUmbers(nums):
    evenNumberList = []
    
    for num in nums:
        if num % 2 == 0 :
            evenNumberList.append(num)
    return evenNumberList

print(keepEvenNUmbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))