def count_sort(arr :list) -> list:
  rv = list()
  con = {k:arr.count(k) for k in range(min(arr), max(arr)+1)}
  for i, v in con.items():
    _ = [i] * v
    rv.extend(_)
  return rv
