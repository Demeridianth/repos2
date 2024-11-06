import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        """Set up a new shopping cart for each test."""
        self.cart = ShoppingCart()

    def test_add_item(self):
        item = Item("Apple", 0.99)
        self.cart.add_item(item)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.total_price(), 0.99)

    def test_remove_item(self):
        item = Item("Banana", 0.50)
        self.cart.add_item(item)
        self.cart.remove_item("Banana")
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.total_price(), 0)

    def test_total_price(self):
        item1 = Item("Apple", 0.99)
        item2 = Item("Orange", 1.50)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.assertEqual(self.cart.total_price(), 2.49)

    def test_list_items(self):
        item1 = Item("Apple", 0.99)
        item2 = Item("Banana", 0.50)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        items = self.cart.list_items()
        self.assertIn("Item(name: Apple, price: 0.99)", items)
        self.assertIn("Item(name: Banana, price: 0.50)", items)

    def test_remove_non_existing_item(self):
        item = Item("Apple", 0.99)
        self.cart.add_item(item)
        self.cart.remove_item("Banana")  # Item does not exist
        self.assertEqual(len(self.cart.items), 1)  # No item should be removed
        self.assertEqual(self.cart.total_price(), 0.99)

    def test_empty_cart(self):
        self.assertEqual(self.cart.total_price(), 0)
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.list_items(), [])

if __name__ == '__main__':
    unittest.main()
