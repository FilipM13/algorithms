def linear(arr, value):
  for n, v in enumerate(arr):
    if v == value:
      return n
  return None