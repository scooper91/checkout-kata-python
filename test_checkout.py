import pytest
from index import checkout

def test_empty_basket_returns_0():
  assert checkout('') == 0

single_items = [['A', 50], ['B', 30], ['C', 20], ['D', 15]]

@pytest.mark.parametrize('item_price', single_items)
def test_single_item_returns_price(item_price):
  item, price = item_price
  assert checkout(item) == price

multiple_items = [['ABCDA', 165], ['CBA', 100], ['DABCC', 135]]

@pytest.mark.parametrize('multiple_item_price', multiple_items)
def test_multiple_items_returns_total_price(multiple_item_price):
  items, total = multiple_item_price
  assert checkout(items) == total
