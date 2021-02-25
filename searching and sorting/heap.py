class Node:

  def __init__(self, value = None):
    self.value = value
    self.child1 = None
    self.child2 = None

  def switch(self) -> None:
    if self.child1 is not None:
      self.child1.switch()
      if self.value < self.child1.value:
        self.value, self.child1.value = self.child1.value, self.value

    if self.child2 is not None:
      self.child2.switch()
      if self.value < self.child2.value:
        self.value, self.child2.value = self.child2.value, self.value

  def count_children(self) -> int:
    rv = 0
    if self.value is not None:
      rv += 1
    if self.child1 is not None:
      rv += self.child1.count_children()
    if self.child2 is not None:
      rv += self.child2.count_children()
    return rv

  def add_value(self, new) -> None:
    if self.value is None:
      self.value = new
    elif self.child1 is None:
      self.child1 = Node(new)
    elif self.child2 is None:
      self.child2 = Node(new)
    elif self.child1.count_children() <= self.child2.count_children():
      self.child1.add_value(new)
    elif self.child2.count_children() < self.child1.count_children():
      self.child2.add_value(new)

  def __repr__(self):
    return f'({self.value}, [{self.child1}, {self.child2}])'

def heap_sort(arr :list) -> list:
  rv = list()
  while len(arr) > 0:
    root = Node()
    for a in arr:
      root.add_value(a)
    root.switch()
    rv.insert(0, root.value)
    arr.remove(root.value)
  return rv
