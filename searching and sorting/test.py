"""
Basic tests for searching and sorting algorithms.
"""
import random
from termcolor import cprint

def sort_test(f, n :int = 10, v_min :int = 0, v_max :int = 100) -> None:
  """
  Tests sorting algorithm.
  :param f: function - sorting function to be tested
  :param n: int - number of tests
  :param v_max: int - maximum value of an array
  :param v_min: int - minimum value of an array
  :return: None
  """
  for i in range(n):
    ar = list(range(v_min, v_max+1))
    random.shuffle(ar)
    goal = sorted(ar)
    result = f(ar)
    gr = zip(goal, result)
    dif = [(i,v) if v[0] != v[1] else True for i,v in enumerate(gr)]
    ver = ''
    for d in dif:
      if d is not True:
        ver += f'{d}\n'
    assert result == goal, f'Test failed. \n{ver}'
  cprint('Passed', 'green')

def search_test(f, n :int = 10, v_min :int = 0, v_max :int = 100) -> None:
  """
  Tests searching algorithm.
  :param f: function - searching function to be tested
  :param n: int - number of tests
  :param v_max: int - maximum value of an array
  :param v_min: int - minimum value of an array
  :return: None
  """
  for i in range(n):
    ar = list(range(v_min, v_max+1))
    target = random.choice(ar)
    goal = ar.index(target)
    result = f(ar, target)
    assert goal == result, f'Test failed, goal = {goal}, result = {result}.'
  cprint('Passed', 'green')

# testing searching algorithms
import linear, binary, jump, interpolation, exponential, ternary
print('Linear search test.')
search_test(linear.linear, 1000, -500, 1000)
print('Binary search test.')
search_test(binary.binary, 1000, -500, 1000)
print('Jump search test.')
search_test(jump.jump, 1000, -500, 1000)
print('Interpolation search test.')
search_test(interpolation.interpolation, 1000, -500, 1000)
print('Exponential search test.')
search_test(exponential.exponential, 1000, -500, 1000)
print('Ternary search test.')
search_test(ternary.ternary, 1000, -500, 1000)

# testing sorting algorithms
import selection, bubble, insertion, merge, quick, heap, count, radix, bucket, shell, comb, cycle
print('Comb sort test.')
sort_test(comb.comb, 100, 100, 0)
print('Selection sort test.')
sort_test(selection.selection, 100, -500, 1000)
print('Bubble sort test.')
sort_test(bubble.bubble, 100, -500, 1000)
print('Insertion sort test.')
sort_test(insertion.insertion, 100, -500, 1000)
print('Merge sort test.')
sort_test(merge.merge, 100, -500, 1000)
print('Quick sort test.')
sort_test(quick.quick, 100, -500, 1000)
print('Count sort test.')
sort_test(count.count_sort, 100, -500, 1000)
print('Radix sort test.')
sort_test(radix.radix, 100, 0, 1000)
print('Bucket sort test.')
sort_test(bucket.bucket, 100, 0, 1000)
print('Shell sort test.')
sort_test(shell.shell, 100, -500, 1000)
print('Cycle sort test.')
sort_test(cycle.cycle, 100, -500, 1000)
print('Heap sort test.')
sort_test(heap.heap_sort, 100, -500, 1000)
