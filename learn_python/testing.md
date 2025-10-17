# Code Testing in Python

## Unit Testing (using unittest)

```py
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
```

## Integration Testing

```py
import unittest

def multiply(a, b):
    return a * b

def calculate_total(prices):
    return sum(prices)

def calculate_discounted_total(prices, discount):
    total = calculate_total(prices)
    return multiply(total, 1 - discount)

class TestIntegration(unittest.TestCase):

    def test_discounted_total(self):
        prices = [10, 20, 30]
        self.assertEqual(calculate_discounted_total(prices, 0.1), 54)
```

## Mocking & Stubbing Dependencies (with unittest.mock)
```py
import requests
from unittest.mock import patch

def fetch_data(url):
    response = requests.get(url)
    return response.json()

class TestAPI(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        mock_get.return_value.json.return_value = {'status': 'ok'}
        result = fetch_data('http://fakeapi.com')
        self.assertEqual(result['status'], 'ok')
```

## Skipping Tests in Python
### With unittest
```py
import unittest
import sys

class TestExample(unittest.TestCase):

    @unittest.skip('Feature not implemented yet')
    def test_not_ready(self):
        self.assertEqual(1, 2)

    @unittest.skipIf(sys.platform == 'win32', 'Does not run on Windows')
    def test_only_non_windows(self):
        self.assertTrue(True)

    @unittest.skipUnless(sys.platform == 'linux', 'Only runs on Linux')
    def test_only_linux(self):
        self.assertTrue(True)
```

### With pytest
```py
import sys
import pytest

@pytest.mark.skip(reason='Feature under development')
def test_skip_example():
    assert 1 == 2

@pytest.mark.skipif(sys.platform == 'win32', reason='Fails on Windows')
def test_not_on_windows():
    assert True

@pytest.mark.xfail(reason='Known bug, expected to fail')
def test_expected_fail():
    assert 1 == 2
```

## Testing for exceptions

```py
# function
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero!")
    return a / b

# test
import pytest

def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="You can't divide by zero!"):
        divide(1, 0)
```

## References
1. https://betterstack.com/community/guides/testing/pytest-fixtures-guide/
2. https://pytest-with-eric.com/fixtures/pytest-fixtures/
3. https://medium.com/@adocquin/mastering-unit-tests-in-python-with-pytest-a-comprehensive-guide-896c8c894304