import insertion

def shell(arr :list, k :int = 1) -> list:
  L = len(arr)
  d = L//(2**k)
  shells = list()
  i = 0
  n = 0

  while True:
    shells.append([])
    while True:
      shells[-1].append(d*n+i)
      n += 1
      if d*n+i >= L:
        n = 0
        i += 1
        break
    if d*n+i >= d:
      break

  for sh in shells:
    temp = [arr[s] for s in sh]
    temp = insertion.insertion(temp)
    for i, s in enumerate(sh):
      arr[s] = temp[i]

  if L//(2**k+1) > 1:
    arr = shell(arr, k+1)

  return arr

import random
ar = list(range(150)) + list(range(20, 70))
random.shuffle(ar)
print(ar)
print(shell(ar))
print(shell(ar) == sorted(ar))