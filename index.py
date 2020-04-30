_items = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
    }

def checkout(items):
  total = 0

  for item in items:
    total += _items[item]

  return total
