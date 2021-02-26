def radix(arr :list, step :int = 1, max_len :int = None) -> list:
  if max_len is None: max_len = len(str(max(arr)))

  d1 = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
  for i in arr:
    try:
      d1[int(str(i)[-step])].append(i)
    except IndexError:
      d1[0].append(i)

  arr = list()
  for i in d1:
    arr.extend(d1[i])

  if step < max_len:
    arr = radix(arr, step+1, max_len)

  return arr
