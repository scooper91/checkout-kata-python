from index import checkout

def test_empty_basket_returns_0():
  assert checkout('') == 0
