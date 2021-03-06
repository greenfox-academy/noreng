import unittest
from menu import *

class TestMenuItem(unittest.TestCase):
    def test_existence(self):
        menu1 = MenuItem('0', 'New Game')

    def test_menu_item_parameters(self):
        menu1 = MenuItem('0', 'New Game')
        self.assertEqual(menu1.id, '0')
        self.assertEqual(menu1.text, 'New Game' )

    def test_menu_item_representation(self):
        menuitem = MenuItem('1', 'Load Game')
        menuitem = str(menuitem)
        self.assertEqual(menuitem, '1 > Load Game')

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.testmenu = Menu([
            MenuItem(1, 'Test', lambda x: True),
            MenuItem(2, 'Test2', lambda x: False)
            ])

    def test_existence(self):
        menu = Menu(MenuItem('0', 'New Game'))

    def test_get_menu_items(self):
        menu = self.testmenu
        self.assertEqual(menu.get_menu(), '1 > Test\n2 > Test2')

if __name__ == "__main__":
    unittest.main()
