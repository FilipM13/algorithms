def quick(arr :list) -> list:
  if len(arr) <= 1: return arr
  pivot = arr[-1]
  border = 0
  for i in range(len(arr)):
    if arr[i] <= pivot:
      arr[i], arr[border] = arr[border], arr[i]
      border += 1
  left = quick(arr[:border-1])
  right = quick(arr[border:])
  return left + [arr[border-1]] + right
