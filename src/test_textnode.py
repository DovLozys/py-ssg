import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Node", TextType.NORMAL)
        node2 = TextNode("Node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("Node", TextType.NORMAL, url=None)
        node2 = TextNode("Node", TextType.NORMAL)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
