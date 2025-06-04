import unittest

from ..main import Inventario


class TestInventario(unittest.TestCase):
    def test_adicionar_item_limite(self):
        inv = Inventario(capacidade_maxima=2)
        self.assertTrue(inv.adicionar_item("potion"))
        self.assertTrue(inv.adicionar_item("sword"))
        self.assertFalse(inv.adicionar_item("shield"))


if __name__ == "__main__":
    unittest.main()
