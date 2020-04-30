_items = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
    }

def checkout(items):
  total = 0
  a_count = 0

  for item in items:
    if item == 'A':
      a_count += 1

    total += _items[item]

  if a_count >= 3:
    total -= 20

  return total
