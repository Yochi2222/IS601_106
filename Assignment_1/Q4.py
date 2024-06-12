def empty_str(arr):
  """Removes empty strings from a list and prints the resulting list.

  Args:
    arr: The list to remove empty strings from.
  """

  print(f'output for arr: \n{list(filter(None, arr))}')  # Filter out empty strings
  print('\n End of empty str values')

arr1 = ['apple', '', 'banana', '', 'cherry']
arr2 = ['', 'dog', '', 'cat', '']
arr3 = ['hello', '', 'world', '', '']
arr4 = ['', '', '', '', '']
arr5 = ['one', '', 'two', '', 'three']

empty_str(arr1)
empty_str(arr2)
empty_str(arr3)
empty_str(arr4)
empty_str(arr5)