array = [(2, 5), (1, 2), (4, 1), (3, 3)]
arr_dic = [
    {"name": "John", "age": 25},
    {"name": "Mary", "age": 30},
    {"name": "Bob", "age": 20}
]
def bubble_sort(array):
  for i in range(len(array)):
    for x in range(len(array)-1):
      if array[x] > array[x+1]:
        array[x], array[x+1] = array[x+1], array[x]
  return array

print(bubble_sort(array))