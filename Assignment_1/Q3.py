def converted_sum_values(arr):
  """Calculates and prints the sum of values in a list after converting negative values to positive.

  Args:
    arr: The list to calculate the sum for.
  """

  # Make a copy of the list to avoid modifying the original
  positive_arr = arr.copy()

  # Convert negative values to positive
  for i in range(len(positive_arr)):
    if positive_arr[i] < 0:
      positive_arr[i] = abs(positive_arr[i])

  total_sum = sum(positive_arr)
  print(f'output for arr: \n{total_sum}')
  print('\n End of converted sum values')

arr1 = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]
arr2 = [5, -8, 13, -21, 34, -55, 89, -144, 233]
arr3 = [-7, 12, -15, 18, -21, 24, -27, 30, -33]
arr4 = [11, -22, 33, -44, 55, -66, 77, -88, 99]
arr5 = [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30]

converted_sum_values(arr1)
converted_sum_values(arr2)
converted_sum_values(arr3)
converted_sum_values(arr4)
converted_sum_values(arr5)