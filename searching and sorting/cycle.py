def cycle(arr :list) -> list:
  target = map(lambda x: sum(i<x for i in arr), arr)
  permutation = dict(zip(arr, target))
  arr = [None] * len(arr)
  for i, v in permutation.items():
    arr[v] = i
  return arr
