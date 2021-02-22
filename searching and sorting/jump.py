from linear import linear

def jump(arr :list, value, step :int = None) -> int:
  if step is None: step = int(len(arr)**0.5)
  max_jumps = len(arr)//step - 1
  for i in range(max_jumps):
    if arr[i*step] <= value < arr[(i+1)*step]:
      return linear(arr[i*step : (i+1)*step], value) + i*step
  return linear(arr[max_jumps:], value) + max_jumps
