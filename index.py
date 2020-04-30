_items = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
    }

def _calculate_discount(quantity, quantity_needed, discount):
  return (quantity // quantity_needed) * discount

def checkout(items):
  item_counts = {}

  def item_count(item):
    return item_counts.get(item, 0)

  total = 0

  for item in items:
    item_counts[item] = item_count(item) + 1

    total += _items[item]

  a_discount = _calculate_discount(item_count('A'), 3, 20)
  b_discount = _calculate_discount(item_count('B'), 2, 15)

  total -= a_discount + b_discount

  return total
