def comb(arr :list, gap :int = None) -> list:
  if gap is None: gap = len(arr)
  i = 0
  while True:
    try:
      if arr[i] > arr[gap+i]:
        arr[i], arr[gap+i] = arr[gap+i], arr[i]
    except IndexError:
      break
    i += 1
  g2 = int(gap/1.3)
  if g2 >= 1:
    arr = comb(arr, g2)
  return arr
