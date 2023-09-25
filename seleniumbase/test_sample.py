# This requires a browser driver, e.g., chromedriver
from seleniumbase import BaseCase
import pytest

class VisualTest(BaseCase):
    def test_visual(self):
        self.open('https://www.lambdatest.com/selenium-playground/simple-form-demo')
        self.check_window(name="main_window")

# This code block ensures that the test runs if this script is executed directly.
if __name__ == "__main__":
    pytest.main()