def selection(arr :list) -> list:
  sorted_list = list()
  while len(arr) != 0:
    i = arr.index(min(arr))
    sorted_list.append(arr[i])
    del arr[i]
  return sorted_list
