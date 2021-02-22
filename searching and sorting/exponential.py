from binary import binary

def exponential(arr :list, value) -> int:
  if arr[0] == value: return 0
  _i = 1
  while _i < len(arr) and arr[_i] <= value:
    _i *= 2
  return binary(arr=arr, value=value, end=min(_i, len(arr) - 1), start=int(_i / 2))
