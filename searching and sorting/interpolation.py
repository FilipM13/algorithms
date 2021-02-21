def interpolation(arr :list, value) -> int:
  start = 0
  end = len(arr)-1
  if arr[start] == value: return start
  if arr[end] == value: return end
  while arr[start] < value < arr[end] and start <=end:
    position = start + int(((float(end - start) / ( arr[end] - arr[start])) * ( value - arr[start])))
    if value == arr[position]:
      return position
    elif value > arr[position]:
      start += 1
    elif value < arr[position]:
      end -= 1
  return -1
