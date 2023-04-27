"""
1-Write a Python program to create an array of 5 integers and display the array items. Access each element and print it.

2-Write a Python program to find the sum of all elements of an array.

3-Write a Python program to find the largest and smallest element in an array.

4-Write a Python program to find the second largest element in an array.

5-Write a Python program to remove the duplicate elements in an array.
"""

# 1
#I use the random module for create 5 random integers (1, 10), but also I can create a array with the integers 1,2,3,4,5

import array as arr
import random as rd

five_array = arr.array("i", [])
for i in range(6):
    five_array.append(rd.randint(1,10))
    print(f"Array[{i}] = {five_array[i]}")

print(f"All array: {five_array}")


# 2
#In this solutions I don't use sum() for obviously reason and I use the five_array

def array_sum(array_s):
    result = 0
    for i in array_s:
        result += i
    return result
print(f"the sum for this array is {array_sum(five_array)}")

# 3
#I use this logic
# example: array = arr.array("i", [5, 6, 3, 8, 1])
# array[0] < array[1]

def largest_smaller(array_ls):
    largest = 0
    smallest = 0
    for i in array_ls:
        # largest
        if i >= largest:
            largest = i
        elif i <= smallest or smallest == 0:
            smallest = i
    return f"smallest: {smallest}, largest: {largest}"

print(largest_smaller(five_array))

# 4
# I can't solve that help ;-;
array_mio = [9, 5, 2, 5, 8, 2]
def second_largest(array_s):
    first = 0
    second = -1
    for i in array_s:
        if i >= first:
            first = i
        if second < i and first != i or second < i and i == array_s[0]:
            second = i
    if second == first:
        second = -1
        array_s.pop(0)
        for i in array_s:
            if second < i and first != i:
                second = i
            
    return second
print(f"the second largest number is: {second_largest(five_array)}")