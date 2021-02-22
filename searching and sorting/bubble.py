def bubble(arr :list) -> list:
  passed = False
  while not passed:
    passed = True
    for i, v in enumerate(arr[:-1]):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        passed = False
  return arr
