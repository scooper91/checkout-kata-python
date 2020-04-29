from index import checkout

def test_empty_basket_returns_0():
  assert checkout('') == 0

def test_single_a_returns_50():
  assert checkout('A') == 50

def test_single_b_returns_30():
  assert checkout('B') == 30

def test_single_c_returns_20():
  assert checkout('C') == 20

def test_single_d_returns_15():
  assert checkout('D') == 15
