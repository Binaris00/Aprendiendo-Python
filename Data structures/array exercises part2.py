"""
1-Write a Python program to reverse an array.

2-Write a Python program to rotate an array of n elements to the right by k steps.

3-Write a Python program to find the intersection of two arrays.

4-Write a Python program to find the union of two arrays.

5-Write a Python program to find the kth largest element in an unsorted array.

6-Write a Python program to find the kth smallest element in a sorted array.

7-Write a Python program to find the first non-repeating element in an array.

8-Write a Python program to find the contiguous subarray with maximum sum.

9-Write a Python program to sort an array of 0's, 1's and 2's.

10-Write a Python program to merge two sorted arrays.
"""

import array as arr

# 1
good_array = arr.array("i", [1, 2, 3, 4, 5])
good_array = arr.array("i", [5, 1, 2, 3, 4])
"""
def inversed_array(par_arr):
    new_reversed_array = arr.array("i", [])
    for i in par_arr[::-1]:
        new_reversed_array.append(i)

    return new_reversed_array
"""
def inversed_array(arr):
    n = len(arr)
    
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr

# 2

def rotate_array(array, times):
    n = len(array)
    times = times % n # handle case when times is greater than n
    for i in range(times):
        for j in range(n-1):
            array[j], array[j+1] = array[j+1], array[j]    
    return array

print(rotate_array([1, 2, 3, 4, 5], 2)) # Output: [4, 5, 1, 2, 3]
