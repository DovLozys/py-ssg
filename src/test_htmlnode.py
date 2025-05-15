import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "id": "top"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" id="top"',
        )

    def test_values(self):
        node = HTMLNode(
            "p",
            "Just placeholder text",
        )
        self.assertEqual(
            node.tag,
            "p",
        )
        self.assertEqual(
            node.value,
            "Just placeholder text",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "span",
            "very bold",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(span, very bold, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()
