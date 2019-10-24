#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
      if items[i] > items[i + 1]:
        return False
    return True



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    if len(items) < 2:
      return True
    unsorted = True
    swaps = 0
    sorted_spots = 1
    while unsorted:
      swaps = 0
      for i in range(len(items) - sorted_spots):
        if items[i] > items[i + 1]:
          items[i], items[i + 1] = items[i + 1], items[i]
          swaps += 1
      if swaps == 0:
        unsorted = False
      sorted_spots += 1

  

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    if len(items) < 2:
      return True
    list_min = 0
    for i in range(len(items) - 1):
      list_min = i
      for j in range(i + 1, len(items)):
        if items[j] < items[list_min]:
          list_min = j
      items[list_min], items[i] =  items[i], items[list_min]
          

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    if len(items) < 2:
      return True
      # traverse from 1 through the array
    for i in range(1, len(items)):
      curr_min = items[i]

      j = i-1
      while j >= 0 and curr_min < items[j]:
        items[j + 1] = items[j]
        j -= 1
      items[j + 1] = curr_min

if __name__ == "__main__":
    
  items =  [6, 4, 3, 2, 1, -1]
  insertion_sort(items)
  print(items)