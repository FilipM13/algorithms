def merge(arr :list) -> list:
  if len(arr) > 1:
    mid = len(arr)//2
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    rv = list()
    while len(left) > 0 and len(right) > 0:
      if left[0] <= right[0]:
        rv.append(left[0])
        left.remove(left[0])
      else:
        rv.append(right[0])
        right.remove(right[0])
    while len(left) > 0:
      rv.append(left[0])
      left.remove(left[0])
    while len(right) > 0:
      rv.append(right[0])
      right.remove(right[0])
    return rv
  else:
    return arr
