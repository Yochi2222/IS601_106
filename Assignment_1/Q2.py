def sum_values(arr):
  """Calculates and prints the sum of values in a list.

  Args:
    arr: The list to calculate the sum for.
  """

  total_sum = sum(arr)
  print(f'output for arr: \n{total_sum}')
  print('\n End of sum values')

arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
arr2 = [17, 19, 15, 16, 14, 18, 13, 12, 11, 20]
arr3 = [55, 66, 77, 88, 99, 11, 22, 33, 44]

sum_values(arr1)
sum_values(arr2)
sum_values(arr3)