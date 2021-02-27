def pigeonhole(arr: list) -> list:
  m = min(arr)
  M = max(arr)
  rg = M - m +1
  holes = [[] for _ in range(rg)]
  for v in arr:
    holes[v - m].append(v)
  arr = list()
  print(holes)
  for h in holes:
    arr.extend(h)
  return arr

