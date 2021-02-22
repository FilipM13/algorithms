def selection(arr :list) -> list:
  sorted_list = list()
  unsorted_list = arr
  while len(unsorted_list) != 0:
    i = unsorted_list.index(min(unsorted_list))
    sorted_list.append(unsorted_list[i])
    del unsorted_list[i]
  return sorted_list
