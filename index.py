_items = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
    }

def checkout(items):
  return _items.get(items, 0)
