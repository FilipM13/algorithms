def comb(arr :list, gap :int = None) -> list:
  if gap is None: gap = len(arr)-1
  i = 0
  while True:
    while True:
      try:
        if arr[0+i] > arr[gap+i]:
          arr[0+i], arr[gap+i] = arr[gap+i], arr[0+i]
        i += 1
      except IndexError:
        i += 1
        break
    if i >= gap:
      break
  g2 = int(gap//1.3)
  if g2 >= 1:
    arr = comb(arr, g2)
  return arr
