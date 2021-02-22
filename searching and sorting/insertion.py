def insertion(arr :list) -> list:
  print(arr)
  for i, value in enumerate(arr[1:]):
    j = i
    if value < arr[j]:
      while value < arr[j] and j >= 0:
        j -= 1
      arr.insert(j+1, value)
      del arr[i+2]
  return arr
