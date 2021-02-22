def binary(arr :list, value, end :int, start :int = 0) -> int:
  middle = int((start + end) / 2)
  if value == arr[middle]:
    return middle
  elif value > arr[middle]:
    return binary(arr, value, end, middle + 1)
  elif value < arr[middle]:
    return binary(arr, value, value, start)
