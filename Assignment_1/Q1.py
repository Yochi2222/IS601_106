
def odd_values(arr):
  """Prints the odd values in a list.

  Args:
    arr: The list to print the odd values from.
  """

  print(f'output for arr: \n')
  for num in arr:
    if num % 2 != 0:
      print(num)
  print('\n End of odd values')

arr1 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48]
arr2 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48]
arr3 = [15, 13, 16, 12, 17, 11, 18, 10, 19, 9]

odd_values(arr1)
odd_values(arr2)
odd_values(arr3)
