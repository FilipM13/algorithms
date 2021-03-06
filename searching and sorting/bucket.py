import insertion

def bucket(arr :list) -> list:
  M = max(arr)
  L = 10
  buck = [[] for _ in range(L+1)]

  for i in arr:
    buck[int(L * i/M)].append(i)

  for i, v in enumerate(buck):
    buck[i] = insertion.insertion(v)

  rv = list()
  for b in buck:
    rv.extend(b)

  return rv
