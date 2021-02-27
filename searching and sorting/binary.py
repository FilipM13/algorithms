def binary(arr :list, value, start :int = 0, end :int = None) -> int:
  if end is None: end = len(arr)-1
  if arr[start] == value: return start
  if arr[end] == value: return end
  middle = int((start + end) / 2)
  if value == arr[middle]:
    return middle
  elif value > arr[middle]:
    return binary(arr, value, middle, end)
  elif value < arr[middle]:
    return binary(arr, value, start, middle)
