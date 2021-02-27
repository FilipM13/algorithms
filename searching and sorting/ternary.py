def ternary(arr :list, value, start: int = None, end :int = None) -> int or None:
  if start is None: start = 0
  if end is None: end = len(arr)-1
  if arr[start] == value: return start
  if arr[end] == value: return end
  mid1 = 1 + end//3
  mid2 = mid1 + end//3

  if arr[mid1] == value:
    return mid1
  elif arr[mid2] == value:
    return mid2
  elif arr[start] < value < arr[mid1]:
    return ternary(arr=arr, value=value, start=start+1, end=mid1)
  elif arr[mid1] < value < arr[mid2]:
    return ternary(arr=arr, value=value, start=mid1+1, end=mid2-1)
  elif arr[mid2] < value < arr[end]:
    return ternary(arr=arr, value=value, start=mid2, end=end-1)
  else: return None
