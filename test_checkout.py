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

@pytest.mark.parametrize('items_total', multiple_items)
def test_multiple_items_returns_total_price(items_total):
  items, total = items_total
  assert checkout(items) == total

single_a_discount_items = [['AAA', 130], ['ABACAD', 195], ['AAAA', 180]]

@pytest.mark.parametrize('items_total', single_a_discount_items)
def test_returns_total_price_with_one_a_discount(items_total):
  items, total = items_total
  assert checkout(items) == total

multiple_a_discount_items = [['AAAAAA', 260], ['ABAACAAAD', 325], ['AAAAAAAA', 360]]

@pytest.mark.parametrize('items_total', multiple_a_discount_items)
def test_returns_total_price_with_multiple_a_discounts(items_total):
  items, total = items_total
  assert checkout(items) == total
