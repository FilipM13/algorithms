def linear(arr :list, value) -> int:
  for n, v in enumerate(arr):
    if v == value:
      return n
  return -1