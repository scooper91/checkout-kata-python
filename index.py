_items = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
    }

def checkout(items):
  total = 0
  a_count = 0
  b_count = 0

  for item in items:
    if item == 'A':
      a_count += 1

    if item == 'B':
      b_count += 1

    total += _items[item]

  a_discount = (a_count // 3) * 20
  total -= a_discount

  b_discount = (b_count // 2) * 15
  total -= b_discount

  return total
